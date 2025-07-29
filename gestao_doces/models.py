from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to='categoria_imagens/')

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="produtos")
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome


class ImagemProduct(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name="imagens")
    imagem = models.ImageField(upload_to='imagens/')

# Cada usuario tem um carrinho. Esse carrinho só vai ter uma linha que é o 'cliente'
