from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tipoproducto/', views.insertarTipoProducto, name='insertar_tipoproducto'),
    path('vertipoproducto/', views.getTipoProducto, name='get_producto'),
    path('crearproducto/', views.insertarProducto, name='insertar_producto'),
    path('productos/', views.Productos, name='productos'),
    path('editarproducto/', views.modelimProducto, name='modelim_producto'),
    path('editarP/<str:pk>/', views.editarProducto, name='editar_producto'),
    path('eliminarP/<str:pk>/', views.eliminarProducto, name='eliminar_producto'),
    path('tiposervicio/', views.insertarTipoServicio, name='insertar_tiposervicio'),
    path('crearservicio/', views.insertarServicio, name='insertar_servicio'),
    path('servicios/', views.Servicios, name='servicios'),
    path('editarservicio/', views.modelimServicio, name='modelim_servicio'),
    path('editarS/<str:pk>/', views.editarServicio, name='editar_servicio'),
    path('eliminarS/<str:pk>/', views.eliminarServicio, name='eliminar_servicio'),
]