from django.urls import path, include
from inv.views import CategoriaView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('categorias/',CategoriaView.as_view(), name='categoria_list'),
]