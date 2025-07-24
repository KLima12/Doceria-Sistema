from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('register_categoria/', views.register_categoria,
         name="register_categoria"),
    path('view_all_categoria/', views.view_all_categoria,
         name="view_all_categoria"),
    path('view_specific_category/<int:id>',
         views.view_specific_category, name="view_specific_category"),
    path('login/', views.login, name="login"),
    path('register_product/', views.register_product, name="register_product"),
    #     path('view_product/', views.view_product, name="view_product"),
]
