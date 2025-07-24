from django import forms
from django.forms import Textarea
from .models import Categoria, Produto, ImagemProduct


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


class ImagemForm(forms.ModelForm):
    class Meta:
        model = ImagemProduct
        fields = ['imagem']


class LoginForm(forms.Form):
    username = forms.CharField(label="Nome do Úsuario", max_length=20)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
