from django.contrib import admin
from productos.models import Producto, Devolucion
from import_export.admin import ImportExportModelAdmin

class AdminProducto(ImportExportModelAdmin, admin.ModelAdmin):    
    list_display = ["nombre", "imagen", "cantidad"]
    search_fields = ["nombre"]
    class Meta:
        model = Producto    

class AdminDevolucion(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id_devolucion"]
    search_fields = ["id_devolucion"]
    class Meta:
        model = Devolucion

admin.site.register(Producto, AdminProducto)
admin.site.register(Devolucion, AdminDevolucion)
