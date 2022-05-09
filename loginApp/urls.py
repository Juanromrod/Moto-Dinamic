from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('registrar_usuario/', views.register_user, name='registrar_usuario'),
    path('buscar_usuario/', views.modelimUsuario, name='buscar_usuario'),
    path('editarU/<str:pk>/', views.editarUsuario, name='editar_usuario'),
    path('eliminarU/<str:pk>/', views.eliminarUsuario, name='eliminar_usuario'),

]