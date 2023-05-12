from django.contrib import admin
from facturas.models import Detalle_Factura


class AdminDetalleFac(admin.ModelAdmin):
    list_display = ["cod_fac"]
    search_fields = ["cod_fac"]
    class Meta:
        model = Detalle_Factura

admin.site.register(Detalle_Factura, AdminDetalleFac)
