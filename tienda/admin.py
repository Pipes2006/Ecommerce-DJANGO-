from django.contrib import admin
from .models import Cliente, CategoriaProducto, Producto, Pedido, DetallePedido, Pago
from django.utils.html import format_html

admin.site.register(Cliente)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0
    readonly_fields = (
        'nombre_cliente',
        'apellidos_cliente',
        'email_cliente',
        'telefono_cliente',
        'direccion_cliente',
    )

    def nombre_cliente(self, obj):
        return obj.pedido.cliente.nombre if obj.pedido and obj.pedido.cliente else ""
    def apellidos_cliente(self, obj):
        return obj.pedido.cliente.apellido if obj.pedido and obj.pedido.cliente else ""
    def email_cliente(self, obj):
        return obj.pedido.cliente.email if obj.pedido and obj.pedido.cliente else ""
    def telefono_cliente(self, obj):
        return obj.pedido.cliente.telefono if obj.pedido and obj.pedido.cliente else ""
    def direccion_cliente(self, obj):
        return obj.pedido.cliente.direccion if obj.pedido and obj.pedido.cliente else ""

    nombre_cliente.short_description = "Nombre"
    apellidos_cliente.short_description = "Apellidos"
    email_cliente.short_description = "Email"
    telefono_cliente.short_description = "Teléfono"
    direccion_cliente.short_description = "Dirección"

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetallePedidoInline]
    list_display = (
        'identificador',
        'nombre_cliente',
        'direccion_cliente',
        'telefono_cliente',
        'email_cliente',
        'fecha',
        'total',
    )

    def nombre_cliente(self, obj):
        return f"{obj.cliente.nombre} {obj.cliente.apellido}"
    nombre_cliente.short_description = "Cliente"

    def direccion_cliente(self, obj):
        return obj.cliente.direccion
    direccion_cliente.short_description = "Dirección"

    def telefono_cliente(self, obj):
        return obj.cliente.telefono
    telefono_cliente.short_description = "Teléfono"

    def email_cliente(self, obj):
        return obj.cliente.email
    email_cliente.short_description = "Email"

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

