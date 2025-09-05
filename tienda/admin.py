from django.contrib import admin

from django.contrib import admin
from .models import Cliente, CategoriaProducto, Producto, Pedido, DetallePedido
from .models import Pago

admin.site.register(Cliente)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
	list_display = ("nombre", "telefono", "total", "estado", "fecha")
	list_filter = ("estado", "fecha")
	search_fields = ("nombre", "telefono")
	list_editable = ("estado",)
admin.site.register(Pedido)
admin.site.register(DetallePedido)

