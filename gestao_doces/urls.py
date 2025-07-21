from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('register_categoria/', views.register_categoria,
         name="register_categoria"),
    path('view_categoria/', views.view_categoria, name="view_categoria"),
]
