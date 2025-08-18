from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import CategoryForm, ProductForm, LoginForm
from .models import Category, ImageProduct, Product
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                # Deixando o úsuario logado ainda quando for redirecionar
                login_django(request, user)
                return redirect("gestao_home")
        else:
            messages.error(request, "Formulário inválido")
    else:
        form = LoginForm()
    return render(request, "gestao/login.html", context={'form': form})


def logout(request):
    auth_logout(request)
    return redirect('gestao_login')


@login_required
def home(request):
    return render(request, "gestao/gestao_home.html")


@login_required
def register_category(request):

    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        print(f"Formulario chegou aqui {form}")
        if form.is_valid():
            # Salvando no banco de dados
            form.save()
            messages.success(request, "Categoria criada com sucessso!")
            # Redirecionando para home de volta
            return redirect("gestao_home")
        else:
            return HttpResponse("Error")
    else:
        form = CategoryForm()

    return render(request, "gestao/register_category.html", context={'form': form})


@login_required
def view_all_categories(request):
    categories = Category.objects.all()
    return render(request, "gestao/view_all_categories.html", context={'categories': categories})


@login_required
def view_specific_category(request, id):
    # Usando get porque retorna uma única instância
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    return render(request, "gestao/view_specific_category.html", context={'category': category, 'products': products})


@login_required
def edit_category(request, id):
    """Edit a Category"""
    category = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None,
                        request.FILES or None, instance=category)
    if form.is_valid():
        form.save()
        messages.success(request, "Catégoria editada com sucesso!")
        return redirect('view_specific_category', id=category.id)
    return render(request, "gestao/edit_category.html", context={"form": form, "category": category})


@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Categoria deletada com sucesso!")
        return redirect("view_all_categories")
    return render(request, "gestao/delete_category.html", context={"category": category})


@login_required
def register_product(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product = product_form.save()
            images = request.FILES.getlist('images')
            for img in images:
                # Interando nas imagens e adicionando no banco de dados
                ImageProduct.objects.create(product=product, images=img)
                print("Imagem criada no banco de dados")
            messages.success(request, "Produto adicionado com sucesso!")

            return redirect("gestao_home")
        else:
            messages.success(
                request, "Produto não registrado! Tente novamente!")
            return redirect("register_product")
    else:
        product_form = ProductForm()
    return render(request, "gestao/register_product.html", context={"product_form": product_form})


@login_required
def view_product(request, id):
    product = get_object_or_404(Product, id=id)
    images = ImageProduct.objects.filter(product=product)
    return render(request, "gestao/view_product.html", context={"product": product, "images": images})


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    # Acessando a imagem relacionada ao produto
    image = ImageProduct.objects.filter(product=product)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST":
        images = request.FILES.getlist("images")
        for img in images:
            ImageProduct.objects.create(product=product, images=img)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto editado com sucesso!")
            return redirect("view_product", product.id)
    return render(request, "gestao/edit_product.html", context={"form": form, "image": image})


@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Produto deletado com sucesso!")
        return redirect('view_all_categories')
    return render(request, "gestao/delete_product.html")


@login_required
def delete_image(request, id):
    image = get_object_or_404(ImageProduct, id=id)
    if request.method == "POST":
        product_id = image.product.id  # Acessando o id do produto para redirecionar depois
        image.delete()
        messages.success(request, "Imagem deletada com sucesso")
        return redirect('edit_product', product_id)
    return render(request, "gestao/delete_imagem.html")
