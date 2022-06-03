from MotoDinamicApp.models import Producto

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregarP(self, producto):
        miProducto = Producto.objects.get(id = producto.id)
        id = str(producto.id) + producto.nombre
        imagen = ''
        try:
            imagen = producto.imagen.url
        except:
            print('No tiene imagen')
        if id not in self.carrito.keys():
            if (imagen != ''):
                self.carrito[id]={
                    "producto_id": producto.id,
                    "nombre": producto.nombre,
                    "acumulado": producto.precio,
                    "cantidad": 1,
                    "imagen": producto.imagen.url,
                } 
            else:
                self.carrito[id]={
                    "producto_id": producto.id,
                    "nombre": producto.nombre,
                    "acumulado": producto.precio,
                    "cantidad": 1,
                }  
        else:
            if self.carrito[id]["cantidad"] < miProducto.stock:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def agregarS(self, servicio):
        id = str(servicio.id) + servicio.nombre
        if id not in self.carrito.keys():
            self.carrito[id]={
                "servicio_id": servicio.id,
                "nombre": servicio.nombre,
                "acumulado": servicio.precio,
                "tipo": servicio.idTipoServicio.nombre,
            }
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminarP(self, producto):
        id = str(producto.id) + producto.nombre
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def eliminarS(self, servicio):
        id = str(servicio.id) + servicio.nombre
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id) + producto.nombre
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminarP(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def getProductos(self):
        productos = []
        for key, value in self.carrito.items():
            try:
                productos.append(value["producto_id"])
            except:
                print('')
        return productos

    def getCantidad(self):
        cant_producto = []
        for key, value in self.carrito.items():
            try:
                cant_producto.append(value["cantidad"])
            except:
                print('')
        return cant_producto

    def getServicios(self):
        servicios = []
        for key, value in self.carrito.items():
            try:
                servicios.append(value["servicio_id"])
            except:
                print('')
        return servicios

    def getIva(self):
        iva = 0
        for key, value in self.carrito.items():
            try:
                iva += value["acumulado"] * (0.19)
            except:
                print('')
        return iva
