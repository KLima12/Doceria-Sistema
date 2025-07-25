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


class Carrinho(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)


class ImagemProduct(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name="imagens")
    imagem = models.ImageField(upload_to='imagens/')


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField(default=1)
