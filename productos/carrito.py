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

    def agregar(self, producto):
        cod_prod = str(producto.cod_prod)
        if cod_prod not in self.carrito.keys():
            self.carrito[cod_prod]={
                "producto_id": producto.cod_prod,
                "nombre": producto.nombre,
                "valor" : producto.valor_venta,
                "acumulado": producto.valor_venta,
                "cantidad": 1,
            }
        else:
            self.carrito[cod_prod]["cantidad"] += 1
            self.carrito[cod_prod]["acumulado"] += producto.valor_venta
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        cod_prod = str(producto.cod_prod)
        if cod_prod in self.carrito:
            del self.carrito[cod_prod]
            self.guardar_carrito()

    def restar(self, producto):
        cod_prod = str(producto.cod_prod)
        if cod_prod in self.carrito.keys():
            self.carrito[cod_prod]["cantidad"] -= 1
            self.carrito[cod_prod]["acumulado"] -= producto.valor_venta
            if self.carrito[cod_prod]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

