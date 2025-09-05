from django.contrib import admin

from django.contrib import admin
from .models import Cliente, CategoriaProducto, Producto, Pedido, DetallePedido
from .models import Pago

admin.site.register(Cliente)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
from django.utils.html import format_html

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
	list_display = ("nombre", "telefono", "total", "estado", "estado_icono", "fecha")
	list_filter = ("estado", "fecha")
	search_fields = ("nombre", "telefono")
	list_editable = ("estado",)

	def estado_icono(self, obj):
		if obj.estado == "confirmado":
			return format_html('<span style="color:green;font-size:1.3em;">✔️</span>')
		else:
			return format_html('<span style="color:#d32f2f;font-size:1.3em;">❌</span>')
	estado_icono.short_description = "Confirmación"
admin.site.register(Pedido)
admin.site.register(DetallePedido)

