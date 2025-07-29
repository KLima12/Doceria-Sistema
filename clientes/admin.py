from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cliente)


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ['cliente']  # exemplo de customização


@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ['carrinho', 'produto', 'quantidade']
