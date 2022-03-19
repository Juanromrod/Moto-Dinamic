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

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=20)
    desc = models.CharField(max_length=128)

class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    desc = models.CharField(max_length=128)

class Cliente(models.Model):
    identificacion = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    celular = models.CharField(max_length=15)
    correo = models.CharField(max_length=128)
    

class Moto(models.Model):
    placa = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)    

class OrdenesDeIngreso(models.Model):
    #foreignkey tipo servico
    #foreignkey tipo cliente
    #foreignkey tipo moto
    desc_problema = models.CharField(max_length=128)
    fecha = models.DateTimeField()

class Factura(models.Model):
    #foreign key cliente
    #foreign key productos
    #foreign key servicios
    fecha = models.DateTimeField()
    iva = models.IntegerField()
    total = models.IntegerField()
