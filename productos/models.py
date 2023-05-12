from django.db import models

class Producto(models.Model):
    cod_prod = models.IntegerField(primary_key=True, verbose_name='Código')
    nombre = models.CharField(max_length=30, blank=True, null=True)
    imagen = models.ImageField(upload_to="productos", null=True)
    cantidad = models.IntegerField(blank=True)
    valor_compra = models.IntegerField(blank=True, null=True)
    valor_venta = models.IntegerField(blank=True, null=True)
    fecha_actualiza = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{}'.format(self.nombre)

     
    

class Devolucion(models.Model):
    id_devolucion = models.IntegerField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)     
    nombre_cliente = models.CharField(max_length=150, blank=True, null=True)     
    motivo = models.CharField(max_length=150, blank=True, null=True)
    estado = models.BooleanField()
    fecha = models.DateTimeField()

    
    