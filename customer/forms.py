from django import forms
from .models import Customer


class RegisterCustomerForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "input-field",
            "placeholder": "Confirme sua senha"
        })
    )

    class Meta:
        model = Customer
        fields = ["name", "email", "password", "confirm_password", "phone"]
        widgets = {
            'name': forms.TextInput(attrs={"class": "input-field", 'placeholder': "Digite seu nome"}),
            'email': forms.EmailInput(attrs={"class": "input-field", 'placeholder': "Digite seu Email"}),
            'password': forms.PasswordInput(attrs={"class": "input-field", "placeholder": "Digite sua senha"}),
            'phone': forms.TextInput(attrs={"class": "input-field", "placeholder": "Digite seu Telefone"}),
        }

    # Validação de senha
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("password")
        confirmar = cleaned_data.get("confirm_password")

        if senha and confirmar and senha != confirmar:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ""  # Removendo o texto do label


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input-field',
        'placeholder': 'Digite seu Email'
    }))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={
        'class': 'input-field',
        'placeholder': 'Digite sua senha',
    }))
