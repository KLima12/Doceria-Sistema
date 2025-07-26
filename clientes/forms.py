from django import forms
from .models import Cliente


class CadastroClienteForm(forms.ModelForm):
    confirmar_senha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Cliente
        fields = ["nome", "email", "confirmar_senha",
                  "senha", "telefone", "rua", "numero", "bairro"]
        widgets = {
            'senha': forms.PasswordInput(),
        }


def clean(self):
    cleaned_data = super().clean()
    senha = cleaned_data.get("senha")
    confirmar = cleaned_data.get("confirmar_senha")

    if senha and confirmar and senha != confirmar:
        raise forms.validationError("As senhas não coincidem.")
