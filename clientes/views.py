from django.shortcuts import render, get_object_or_404, redirect
from gestao_doces.models import Produto, Categoria
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .forms import CadastroClienteForm


def cadastrar_cliente(request):
    if request.method == "POST":
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            # Criando o User com Django com o email
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['senha']
            )

            # Salva o cliente no banco
            cliente.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect(request, "login")
    else:
        form = CadastroClienteForm()
    return render(request, "clientes/cadastrar_cliente.html", context={"form": form})


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
