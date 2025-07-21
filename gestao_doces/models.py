from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to='categoria_imagens/')


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    imagens = models.ImageField(upload_to='imagens/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
