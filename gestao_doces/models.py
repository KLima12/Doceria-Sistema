from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(
        # Um produto vai pertencer a uma categoria.
        Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class ImageProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images")
    images = models.ImageField(upload_to='images/')
