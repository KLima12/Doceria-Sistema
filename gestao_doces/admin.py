from django.contrib import admin
from .models import *


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem')
    search_fiedls = ('nome', 'imagem')
    list_filter = ('nome', 'imagem')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'categoria', 'preco', )
    search_fields = ('nome', 'preco')
    list_filter = ('nome', 'preco')


@admin.register(ImagemProduct)
class ImagemProductAdmin(admin.ModelAdmin):
    list_display = ('produto', 'imagem')
    search_fields = ('produto', 'imagem')
    list_filter = ('produto', 'imagem')
