from django.shortcuts import render, HttpResponse, redirect
from .forms import CategoriaForm, ProdutoForm


def home(request):
    return render(request, "gestao/home.html")


def register_categoria(request):

    if request.method == "POST":
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            # Salvando no banco de dados
            form.save()
            # Redirecionando para view categoria
            return redirect("view_categoria")
        else:
            return HttpResponse("Error")
    else:
        form = CategoriaForm()

    return render(request, "gestao/register_categoria.html", context={'form': form})


def view_categoria(request):
    return render(request, "gestao/view_categoria")
