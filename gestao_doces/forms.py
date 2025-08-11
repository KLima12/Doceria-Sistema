from django import forms
from django.forms import Textarea
from .models import Category, Product, ImageProduct


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "descricao": Textarea(attrs={'cols': 80, 'rows': 10})
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageProduct
        fields = ['image']


class LoginForm(forms.Form):
    username = forms.CharField(label="Nome do Úsuario", max_length=20)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
