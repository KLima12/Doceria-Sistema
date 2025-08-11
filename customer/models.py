from django.db import models
from gestao_doces.models import Product
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    favorites = models.ManyToManyField(
        Product, blank=True, related_name="customer_who_favorited")

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class CartProduct(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(default=1)
