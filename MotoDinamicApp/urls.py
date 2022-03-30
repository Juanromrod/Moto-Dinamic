from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tipoproducto/', views.insertarTipoProducto, name='insertar'),
    path('vertipoproducto/', views.getTipoProducto, name='get_producto'),
    path('productos/', views.products, name='productos'),
]