from django.db import models

class Departamento(models.Model):
	cod_depto = models.IntegerField(primary_key=True)
	nombre_departamento = models.CharField(max_length=30, null=True, verbose_name="Departamento")
	fecha_actualiza = models.DateTimeField()

	def __str__(self):
		return'{}'.format(self.nombre_departamento)

class Municipio(models.Model):
	cod_municipio = models.IntegerField(primary_key=True)
	cod_depto  = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=30, null=True)
	act_usua = models.CharField(max_length=8, blank=True, null=True, verbose_name='Usuario que Registra')
	act_hora = models.CharField(max_length=19, blank=True, null=True, verbose_name='Observaciones')

	def __str__(self):
		return'{}'.format(self.nombre)
	class Meta:
		verbose_name_plural="Division Politica"
		verbose_name="Division Politica"

class Categoria(models.Model):
    cod_categoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)  

    def __str__(self):
        return'{}'.format(self.nombre) 
    



class Artesano(models.Model):
    cod_artesano = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)    
    cod_categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)  
    cod_depto  = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)  
    cod_municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE)
    release_date = models.DateField(verbose_name='Fecha de Ingreso')
    def __str__(self):
        return'{}'.format(self.nombre)

class cliente(models.Model):
    cod_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    documento = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateTimeField()
    rol = models.CharField(max_length=40, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return'{}'.format(self.nombre)


