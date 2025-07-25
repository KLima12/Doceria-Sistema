from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name="home"),
    path('register_categoria/', views.register_categoria,
         name="register_categoria"),
    path('view_all_categoria/', views.view_all_categoria,
         name="view_all_categoria"),
    path('view_specific_category/<int:id>',
         views.view_specific_category, name="view_specific_category"),
    path('edit_category/<int:id>', views.edit_category, name="edit_category"),
    path('delete_category/<int:id>', views.delete_category, name="delete_category"),
    path('register_product/', views.register_product, name="register_product"),
    path('view_product/<int:id>', views.view_product, name="view_product"),
    path('edit_product/<int:id>', views.edit_product, name="edit_product"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),
    path('delete_imagem/<int:id>', views.delete_imagem, name="delete_imagem"),
]
