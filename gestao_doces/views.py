from django.shortcuts import render, HttpResponse, redirect
from .forms import CategoriaForm, ProdutoForm, LoginForm
from .models import Categoria
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
                return redirect("home", username)
        else:
            messages.error(request, "Formulário inválido")
    else:
        form = LoginForm()
    return render(request, "gestao/login.html", context={'form': form})


@login_required
def home(request, username):
    return render(request, "gestao/home.html", context={'username': username})


@login_required
def register_categoria(request):

    if request.method == "POST":
        form = CategoriaForm(request.POST, request.FILES)
        print(f"Formulario chegou aqui {form}")
        if form.is_valid():
            # Salvando no banco de dados
            print(f"Form valido: {form}")
            form.save()  # Salvando formulário no django
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
