from django.urls import path
from . import views
urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path("", views.home, name="home"),
    path("category/", views.view_category, name="view_category"),
    path("view_products/", views.view_products, name="view_products"),
    path("view_product_category/<int:id>", views.view_product_category,
         name="view_product_category"),
    path("view_specific_product/<int:id>", views.view_specific_product,
         name="view_specific_product"),
    path("adicionar-ao-carrinho/<int:id>", views.adicionar_ao_carrinho,
         name="adicionar-ao-carrinho"),
    path("view-cart/", views.view_cart, name="view-cart"),
]
