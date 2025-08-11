from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from gestao_doces.models import *
from django.contrib import messages

from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .forms import RegisterCustomerForm, LoginForm
from .core.send_message import *


def register(request):
    if request.method == "POST":
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            # Criando usuário de autentificação do django
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            # Pegando o nome do úsuario
            user.first_name = form.cleaned_data['name']
            user.save()
            customer.user = user
            customer.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("login")
    else:
        form = RegisterCustomerForm()
    return render(request, "customer/register.html", context={"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            if user:
                login_django(request, user)
                return redirect('home')
        else:
            messages.error(request, "Formulário invalido!")
    else:
        form = LoginForm()
    return render(request, "customer/login.html", context={"form": form})


def logout(request):
    auth_logout(request)
    return redirect('home')


def home(request):
    return render(request, "customer/home.html")


def view_category(request):
    category = Category.objects.all()
    return render(request, "customer/view_category.html", context={"category": category})


def view_product_category(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, "customer/view_product_category.html", context={'category': category})


def view_products(request):
    product = Product.objects.all()
    return render(request, "customer/view_products.html", context={"product": product})


def view_specific_product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "customer/view_specific_product.html", context={"product": product})


@login_required
def add_favorite(request, id):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            if not body_unicode:
                return JsonResponse({"status": "erro", "mensagem": "Corpo da requisição vazio"}, status=400)

            print("Requeste body", request.body)
            data = json.loads(body_unicode)
            favorite = data.get('favorite')

            product = get_object_or_404(Product, id=id)
            customer = get_object_or_404(Customer, user=request.user)

            if favorite:
                customer.favorites.add(product)
            else:
                customer.favorites.remove(product)

            return JsonResponse({"status": "ok"})
        except Exception as e:
            return JsonResponse({"status": "erro", "mensagem": str(e)}, status=400)

    return JsonResponse({"status": "erro", "mensagem": "Método inválido"}, status=405)


@login_required
def view_favorites(request):
    products_favorites = Product.objects.filter(
        customer_who_favorited=request.user)
    return render(request, "customer/view_favorites.html", context={"favorites": products_favorites})


@login_required
def add_to_cart(request, id):
    # Obtendo o úsuario
    if request.method == "POST":
        # Estou pegando o ID do produto e quantidade que meu úsuario quer.
        product = get_object_or_404(Product, id=id)
        amount = int(request.POST.get('amount'))

        # Pegar ou criar o carrinho pro cliente atual
        cart, _ = Cart.objects.get_or_create(customer=request.user)

        # Adicionando ou atualizando item no carrinho.
        # Usei o created porque o django procura no banco de dados se já existe um item no carrinho. Ele retorna True ou False
        item, created = CartProduct.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'amount': amount},
        )
        # Se o created retornar Falso, eu tenho que incrementar a quantidade
        if not created:
            # Incrementando na quantidade.
            item.amount += amount
            item.save()

        messages.success(
            request, "Produto adicionado ao carrinho com sucesso!")
        return redirect("view_products")
    else:
        messages.error(
            request, "Deu algum erro inesperado")
        return redirect("view_products")


@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, customer=request.user)
    # Aqui estou fazendo um filtro pra pegar os itens do carrinho do usuario, pelo carrinho
    itens = CartProduct.objects.filter(cart=cart)
    # Aqui eu peguei o carrinho associado ao usuario logado.

    return render(request, "customer/view_cart.html", context={'itens': itens})


def send_whatsapp(request):
    if request.method == "POST":
        product_ids = request.POST.getlist('product_id')
        amount = request.POST.getlist('amount')
        cart = get_object_or_404(Cart, customer=request.user)
        product_info = []
        adder = []
        sum = 0
        # Usei zip para agrupar elementos.
        for product_ids, amounts in zip(product_ids, amounts):
            product = get_object_or_404(Product, id=product_ids)
            amount = int(amounts)
            adder.append((product.preco, amount))

            # Salvando info para mensagem
            product_info.append((product.name, amount))
            itens = CartProduct.objects.create(
                cart=cart,
                product=product,
                amount=amount,
            )
            itens.save()
            sum = calculate_total(adder)
            # Gerando link com a função
            whatsapp_url = encode_for_whatsapp(product_info, sum)

        # Apagando os itens do carrinho após úsuario enviar pro whatsapp
        CartProduct.objects.filter(cart=cart).delete()
        return redirect(whatsapp_url)


@login_required
def delete_favorite(request, id):
    try:
        customer = get_object_or_404(Customer, user=request.user)
        favorite = get_object_or_404(Product, id=id)
        customer.favoritos.remove(favorite)  # Aqui removo o produto favoritos
        return JsonResponse({"status": "ok"})
    except Exception as e:
        return JsonResponse({"status": "erro", "mensagem": str(e)}, status=400)


@login_required
def delete_product_cart(request, id):
    if request.method == "POST":
        try:
            product = get_object_or_404(Product, id=id)
            cart = get_object_or_404(Cart, customer=request.user)
            item = get_object_or_404(
                CartProduct, product=product, cart=cart)
            item.delete()
            return JsonResponse({"status": "ok"})
        except CartProduct.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Item não encontrado"}, status=404)
    return JsonResponse({"status": "error", "message": "Método inválido"}, status=400)
