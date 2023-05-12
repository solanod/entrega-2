from django.urls import path
from productos.views import tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, listar_producutos

urlpatterns = [
    path('', listar_producutos, name="productos"),    
    path('', tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]





    