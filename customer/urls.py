from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="customer_login"),
    path('logout/', views.logout, name="customer_logout"),
    # Tela de solicitação de redefinição de senha
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='customer/password_reset.html'), name='password_reset'),
    # Tela de suceso apó o envio do email
    path('reset-password-send/', auth_views.PasswordResetDoneView.as_view(
        template_name='customer/password_reset_done.html'), name='password_reset_done'),
    # Tela para o usuário criar a nova senha (após clicar no link do email)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='customer/password_reset_confirm.html'), name='password_reset_confirm'),
    # Tela de sucesso após a redefinição de senha
    path('reset-password-full/', auth_views.PasswordResetCompleteView.as_view(
        template_name='customer/password_reset_complete.html'), name='password_reset_complete'),
    path("", views.home, name="customer_home"),
    path("category/", views.view_category, name="view_category"),
    path("view_products/", views.view_products, name="view_products"),
    path("view_product_category/<int:id>", views.view_product_category,
         name="view_product_category"),
    path("view-favorites/", views.view_favorites, name="view_favorites"),
    path("delete-favorite/<int:id>/",
         views.delete_favorite, name="delete-favorite"),
    path("view_specific_product/<int:id>", views.view_specific_product,
         name="view_specific_product"),
    path("add-to-cart/<int:id>", views.add_to_cart,
         name="add-to-cart"),
    path("favorited-product/<int:id>/",
         views.add_favorite, name="favorited-product"),
    path("view-cart/", views.view_cart, name="view-cart"),
    path("send-whatsapp/", views.send_whatsapp, name="send-whatsapp"),
    path("delete-product/<int:id>/",
         views.delete_product_cart, name="delete-product"),
]
