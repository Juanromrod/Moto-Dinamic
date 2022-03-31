from django.db import models
from django.db.models.deletion import CASCADE,PROTECT,SET_NULL,SET_DEFAULT

# Create your models here.

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=30)

class Producto(models.Model): 
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    desc = models.CharField(max_length=128)
    idTipoProducto = models.ForeignKey(TipoProducto, on_delete=PROTECT)

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=30)

class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    desc = models.CharField(max_length=128)
    idTipoServicio = models.ForeignKey(TipoServicio, on_delete=PROTECT)


class Cliente(models.Model):
    identificacion = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    celular = models.CharField(max_length=15)
    correo = models.CharField(max_length=128)
    direccion = models.CharField(max_length=128)
    

class Moto(models.Model):
    placa = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)    

class OrdenDeIngreso(models.Model):
    desc_problema = models.CharField(max_length=228)
    fecha_ingreso = models.DateTimeField()
    info_adicional = models.CharField(max_length=228)
    idMoto = models.ForeignKey(Moto, on_delete=PROTECT)

class Factura(models.Model):
    fecha = models.DateTimeField()
    iva = models.IntegerField()
    total = models.IntegerField()

class Cliente_Factura(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=PROTECT)
    idFactura = models.ForeignKey(Factura, on_delete=PROTECT)

class Factura_Producto(models.Model):
    idFactura = models.ForeignKey(Factura, on_delete=PROTECT)
    idProducto = models.ForeignKey(Producto, on_delete=PROTECT)

class Factura_Servicio(models.Model):
    idFactura = models.ForeignKey(Factura, on_delete=PROTECT)
    idServicio = models.ForeignKey(Servicio, on_delete=PROTECT)

class OrdenDeIngreso_Servicio(models.Model):
    idOrdenDeIngreso = models.ForeignKey(OrdenDeIngreso, on_delete=PROTECT)
    idServicio = models.ForeignKey(Servicio, on_delete=PROTECT)

