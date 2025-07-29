from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from gestao_doces.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .forms import CadastroClienteForm, LoginForm


def cadastro(request):
    if request.method == "POST":
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            # Criando usuário de autentificação do django
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['senha']
            )

            # Pegando o nome do úsuario
            user.first_name = form.cleaned_data['nome']
            user.save()
            cliente.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("login")
    else:
        form = CadastroClienteForm()
    return render(request, "clientes/cadastro.html", context={"form": form})


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
    return render(request, "clientes/login.html", context={"form": form})


def logout(request):
    auth_logout(request)
    return redirect('home')


def home(request):
    return render(request, "clientes/home.html")


def view_category(request):
    category = Categoria.objects.all()
    return render(request, "clientes/view_category.html", context={"category": category})


def view_product_category(request, id):
    category = get_object_or_404(Categoria, id=id)
    return render(request, "clientes/view_product_category.html", context={'category': category})


def view_products(request):
    product = Produto.objects.all()
    return render(request, "clientes/view_products.html", context={"product": product})


def view_specific_product(request, id):
    product = get_object_or_404(Produto, id=id)
    return render(request, "clientes/view_specific_product.html", context={"product": product})


def adicionar_ao_carrinho(request, id):
    # Obtendo o úsuario
    if request.method == "POST":
        # Estou pegando o ID do produto e quantidade que meu úsuario quer.
        produto = get_object_or_404(Produto, id=id)
        quantidade = int(request.POST.get('quantidade'))

        # Pegar ou criar o carrinho pro cliente atual
        carrinho, _ = Carrinho.objects.get_or_create(cliente=request.user)

        # Adicionando ou atualizando item no carrinho.
        # Usei o created porque o django procura no banco de dados se já existe um item no carrinho. Ele retorna True ou False
        item, created = ItemCarrinho.objects.get_or_create(
            carrinho=carrinho,
            produto=produto,
            defaults={'quantidade': quantidade},
        )
        # Se o created retornar Falso, eu tenho que incrementar a quantiade
        if not created:
            # Incrementando na quantidade.
            item.quantidade += quantidade
            item.save()

        messages.success(
            request, "Produto adicionado ao carrinho com sucesso!")
        return redirect("view_products")
    else:
        messages.error(
            request, "Deu algum erro inesperado")
        return redirect("view_products")


def view_cart(request):
    carrinho = get_object_or_404(Carrinho, cliente=request.user)
    # Aqui estou fazendo um filtro pra pegar os itens do carrinho do usuario, pelo carrinho
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)
    # Aqui eu peguei o carrinho associado ao usuario logado.

    return render(request, "clientes/view_cart.html", context={'itens': itens})


def send_whatsapp(request):
    if request.method == "POST":
        produto_ids = request.POST.getlist('produto_id')
        quantidades = request.POST.getlist('quantidade')
        carrinho = get_object_or_404(Carrinho, cliente=request.user)
        # Usei zip para agrupar elementos.
        for produto_id, quantidade in zip(produto_ids, quantidades):
            produtos = get_object_or_404(Produto, id=produto_id)
            quantidade = int(quantidade)

            itens = ItemCarrinho.objects.create(
                carrinho=carrinho,
                produto=produtos,
                quantidade=quantidade
            )

            itens.save()

            

    return HttpResponse("Pegou")
