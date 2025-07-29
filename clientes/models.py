from django.db import models
from gestao_doces.models import Produto
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    favoritos = models.ManyToManyField(
        Produto, blank=True, related_name="clientes_que_favoritaram")
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    def endereco_completo(self):
        # Usei aqui para chamar na view;
        return f"Rua {self.rua}, número {self.numero}, Bairro {self.bairro}"


class Carrinho(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

# Aqui, os úsuarios terão um item no carrinho.


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField(default=1)
