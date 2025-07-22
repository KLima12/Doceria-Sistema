from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('register_categoria/', views.register_categoria,
         name="register_categoria"),
    path('view_all_categoria/', views.view_all_categoria,
         name="view_all_categoria"),
    path('login/', views.login, name="login"),
]
