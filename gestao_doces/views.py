from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import CategoriaForm, ProdutoForm, LoginForm, ImagemForm
from .models import Categoria, ImagemProduct, Produto
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
                return redirect("home")
        else:
            messages.error(request, "Formulário inválido")
    else:
        form = LoginForm()
    return render(request, "gestao/login.html", context={'form': form})


@login_required
def home(request):
    return render(request, "gestao/home.html")


@login_required
def register_categoria(request):

    if request.method == "POST":
        form = CategoriaForm(request.POST, request.FILES)
        print(f"Formulario chegou aqui {form}")
        if form.is_valid():
            # Salvando no banco de dados
            form.save()
            messages.success(request, "Categoria criada com sucessso!")
            # Redirecionando para home de volta
            return redirect("home")
        else:
            return HttpResponse("Error")
    else:
        form = CategoriaForm()

    return render(request, "gestao/register_categoria.html", context={'form': form})


@login_required
def view_all_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, "gestao/view_all_categoria.html", context={'categorias': categorias})


@login_required
def view_specific_category(request, id):
    # Usando get porque retorna uma única instância
    categoria = get_object_or_404(Categoria, id=id)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, "gestao/view_specific_category.html", context={'categoria': categoria, 'produtos': produtos})


@login_required
def register_product(request):
    if request.method == "POST":
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            produto = produto_form.save()
            imagens = request.FILES.getlist('imagens')
            for img in imagens:
                print(f"Imagem sendo interaddas {img}")
                # Interando nas imagens e adicionando no banco de dados
                ImagemProduct.objects.create(produto=produto, imagem=img)
                print("Imagem criada no banco de dados")
            messages.success(request, "Produto adicionado com sucesso!")

            return redirect("home")
        else:
            messages.success(
                request, "Produto não registrado! Tente novamente!")
            return redirect("register_product")
    else:
        produto_form = ProdutoForm()
    return render(request, "gestao/register_product.html", context={"produto_form": produto_form})

# @login_required
# def view_product(request):
#     produto =
