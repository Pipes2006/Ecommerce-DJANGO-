from django.contrib import admin

from django.contrib import admin
from .models import Cliente, CategoriaProducto, Producto, MetodoPago, Pedido, DetallePedido

admin.site.register(Cliente)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(MetodoPago)
admin.site.register(Pedido)
admin.site.register(DetallePedido)

