from itertools import product
from math import prod
from MotoDinamicApp.models import Ciudad, Factura, Producto, TipoProducto, Cliente, Ciudad, Cliente_Factura, Factura_Producto
import pytest
from datetime import datetime
from  MotoDinamicApp.models import Producto

@pytest.mark.django_db
def test_creacion_producto():
    producto = Producto.objects.create(
        nombre = 'Casco',
        precio = 40000,
        stock = 5,
        desc = 'Casco para moto',
        idTipoProducto = TipoProducto.objects.create(nombre='accesorio'),
    )
    assert producto.precio == 40000
    return producto


@pytest.mark.django_db
def test_creacion_cliente():
    cliente = Cliente.objects.create(
        identificacion = '1111',
        nombre = 'Daniel',
        celular = '123456',
        correo = 'daniel@prueba.com',
        ciudad = Ciudad.objects.create(nombre='Cali'),
        direccion = 'Calle 111',
    )
    assert cliente.nombre == 'Daniel'
    return cliente

@pytest.mark.django_db
def test_creacion_factura():
    productoprueba = test_creacion_producto()   
    clienteprueba = test_creacion_cliente()

    factura = Factura.objects.create(
        fecha = datetime.today(),
        iva = 0,
        total = 0,
    )

    cliente_factura = Cliente_Factura.objects.create(
        idCliente = clienteprueba,
        idFactura = factura,
    )

    factura_producto = Factura_Producto.objects.create(
        idFactura = factura,
        idProducto = productoprueba,
        cantidad = 4,
    )

    factura.total = productoprueba.precio * factura_producto.cantidad
    factura.iva = factura.total * 0.19

    assert factura.total == 160000
