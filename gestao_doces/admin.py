from django.contrib import admin
from .models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem')
    search_fiedls = ('nome', 'imagem')
    list_filter = ('nome', 'imagem')
