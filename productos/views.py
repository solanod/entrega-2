from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from productos.models import Producto
from productos.carrito import Carrito
from django.db.models import Q

@login_required
def listar_producutos(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.all()
    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda) 
        ).distinct()  
    return render(request, "productos/tienda.html", {'productos':productos})

@login_required
def tienda(request):    
    productos = Producto.objects.all()
    return render(request, "productos/tienda.html", {'productos':productos})


def inicio(request):    
    return render(request, "partials/inicio.html")

@login_required
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_prod=producto_id)    
    carrito.agregar(producto)
    return redirect("Tienda")
@login_required
def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_prod=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")
@login_required
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_prod=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")
@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")
@login_required
def guardar_carrito(request):
    carrito = Carrito(request)
    carrito.guardar_carrito()
    return redirect("Tienda")
