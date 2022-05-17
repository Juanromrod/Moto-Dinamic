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
        id = str(producto.id) + producto.nombre
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
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
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True