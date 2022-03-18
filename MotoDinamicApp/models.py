from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=20)
    desc = models.CharField(max_length=128)

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField
    desc = models.CharField(max_length=128)
