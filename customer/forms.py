from django import forms
from .models import Customer


class RegisterCustomerForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ["name", "email", "password", "confirm_password",
                  "phone"]
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            "name": "Nome",
            "password": "Senha",
            "confirm_password": "Confirmar_Senha",
            "phone": "Telefone",
        }


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input-field',
        'placeholder': 'Digite seu Email'
    }))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={
        'class': 'input-field',
        'placeholder': 'Digite sua senha',
    }))


def clean(self):
    cleaned_data = super().clean()
    senha = cleaned_data.get("senha")
    confirmar = cleaned_data.get("confirmar_senha")

    if senha and confirmar and senha != confirmar:
        raise forms.validationError("As senhas não coincidem.")
