from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tipoproducto/', views.insertarTipoProducto, name='insertar'),
    path('vertipoproducto/', views.getTipoProducto, name='get_producto'),
    path('crearproducto/', views.insertarProducto, name='insertar_producto'),
    path('productos/', views.Product, name='productos'),
    path('hijo/', views.hijo, name='hijo'),
    path('padre/', views.padre, name='padre'),
]