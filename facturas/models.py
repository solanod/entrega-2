from django.db import models
from django.core.exceptions import ValidationError


class Detalle_Factura(models.Model):
    cod_fac = models.IntegerField(primary_key=True)
    detalle_producto = models.CharField(max_length=42, null=True)
    cantidad = models.IntegerField(null=True)
    precio_unitario = models.IntegerField(null=True)
    precio_total = models.IntegerField(null=True)
    cliente = models.CharField (max_length=50, null=True)
    direccion_envio = models.CharField (max_length=150, null=True)
    telefono = models.CharField (max_length=50,null=True)  
    fecha_compra = models.DateTimeField(null=True)
    def __str__(self):
        return'{}'.format(self.cod_fac)

class Metodos_pago(models.Model):
    metodo = models.CharField(max_length=30, blank=True, null=True)