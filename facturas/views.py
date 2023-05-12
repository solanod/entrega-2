from django.shortcuts import render, redirect
from facturas.models import Detalle_Factura
from django.contrib.auth.decorators import login_required
from productos.carrito import Carrito
from productos.models import Producto



# Utilities
from datetime import datetime

@login_required
def factura(request):
    prostop = Producto.objects.all()
    carrito = Carrito(request)
    now = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
    productos = Detalle_Factura.objects.all()        
    return render(request, "facturas/facturas.html", {'prostop':prostop, 'carrito': carrito, 'now': now})

def guardar_carrito(request):
    carrito = Carrito(request)
    carrito.guardar_carrito()
    return redirect("Tienda")
