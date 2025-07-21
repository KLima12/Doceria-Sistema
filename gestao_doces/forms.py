from django import forms
from django.forms import Textarea
from .models import Categoria, Produto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
        widgets = {
            "descricao": Textarea(attrs={'cols': 80, 'rows': 10})
        }
