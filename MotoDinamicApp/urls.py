from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('typeproduct/', views.insertTypeProduct, name='typeproduct'),
]