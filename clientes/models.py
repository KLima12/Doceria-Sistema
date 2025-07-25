from django.db import models
from gestao_doces.models import Produto


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    favoritos = models.ManyToManyField(
        Produto, blank=True, related_name="clientes_que_favoritaram")
