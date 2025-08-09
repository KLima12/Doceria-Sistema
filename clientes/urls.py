from django.urls import path
from . import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    #     path('reset_password/', views.PasswordResetView.as_view(
    #         template_name="clientes/password_reset.html"), name="password_reset"),
    path("", views.home, name="home"),
    path("category/", views.view_category, name="view_category"),
    path("view_products/", views.view_products, name="view_products"),
    path("view_product_category/<int:id>", views.view_product_category,
         name="view_product_category"),
    path("view-favorites/", views.view_favorites, name="view_favorites"),
    path("delete-favorite/<int:id>/",
         views.delete_favorite, name="delete-favorite"),
    path("view_specific_product/<int:id>", views.view_specific_product,
         name="view_specific_product"),
    path("adicionar-ao-carrinho/<int:id>", views.adicionar_ao_carrinho,
         name="adicionar-ao-carrinho"),
    path("favoritar-produto/<int:id>/",
         views.add_favorite, name="favoritar-produto"),
    path("view-cart/", views.view_cart, name="view-cart"),
    path("send-whatsapp/", views.send_whatsapp, name="send-whatsapp"),
    path("delete-product/<int:id>/",
         views.delete_product_cart, name="delete-product"),
]
