from distutils.command.upload import upload
from xml.parsers.expat import model
from django.db import models
from django.db.models.deletion import CASCADE,PROTECT,SET_NULL,SET_DEFAULT

# Create your models here.

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Producto(models.Model): 
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    desc = models.CharField(max_length=128)
    idTipoProducto = models.ForeignKey(TipoProducto, on_delete=PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True, blank=True)

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    desc = models.CharField(max_length=128)
    idTipoServicio = models.ForeignKey(TipoServicio, on_delete=PROTECT)

class Cliente(models.Model):
    identificacion = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    celular = models.CharField(max_length=15)
    correo = models.EmailField(max_length=128)
    ciudad = models.ForeignKey(Ciudad, on_delete=PROTECT)
    direccion = models.CharField(max_length=128)
    

class Moto(models.Model):
    placa = models.CharField(max_length=30, unique=True)
    color = models.CharField(max_length=30)
    kilometraje = models.IntegerField()
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="motos", null=True, blank=True)
    def __str__(self):
        return self.placa    

class OrdenDeIngreso(models.Model):
    desc_problema = models.CharField(max_length=228)
    fecha_ingreso = models.DateTimeField()
    info_adicional = models.CharField(max_length=228)
    idMoto = models.ForeignKey(Moto, on_delete=PROTECT)
    idCliente = models.ForeignKey(Cliente, on_delete=PROTECT, null=True)

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
    cantidad = models.IntegerField()

class Factura_Servicio(models.Model):
    idFactura = models.ForeignKey(Factura, on_delete=PROTECT)
    idServicio = models.ForeignKey(Servicio, on_delete=PROTECT)

class OrdenDeIngreso_Servicio(models.Model):
    idOrdenDeIngreso = models.ForeignKey(OrdenDeIngreso, on_delete=PROTECT)
    idServicio = models.ForeignKey(Servicio, on_delete=PROTECT)

