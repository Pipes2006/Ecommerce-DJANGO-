from django.db import models

# CLIENTE
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# CATEGORIA_PRODUCTO
class CategoriaProducto(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria


# PRODUCTO
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # 👈 NUEVO CAMPO

    def __str__(self):
        return self.nombre
    def __str__(self):
        return self.nombre


# METODO_PAGO

# MODELO DE PAGO
from django.utils import timezone

class Pago(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField(null=True, blank=True)
    carrito = models.TextField(help_text="JSON con los productos y cantidades")
    total = models.DecimalField(max_digits=12, decimal_places=2)
    ESTADO_CHOICES = [
        ("rechazado", "Rechazado (tiempo expirado)"),
        ("pendiente", "Pendiente de confirmar"),
        ("confirmado", "Confirmado"),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pago de {self.nombre} - {self.telefono} - {self.estado}"

    def save(self, *args, **kwargs):
        from tienda.models import Producto
        import json
        # Si el estado cambia a confirmado y antes no era confirmado, descuenta stock
        if self.pk:
            old = Pago.objects.get(pk=self.pk)
            if old.estado != 'confirmado' and self.estado == 'confirmado':
                carrito = json.loads(self.carrito)
                for item in carrito:
                    try:
                        producto = Producto.objects.get(pk=item['id'])
                        producto.stock = max(producto.stock - int(item['cantidad']), 0)
                        producto.save()
                    except Producto.DoesNotExist:
                        pass
        super().save(*args, **kwargs)


# PEDIDO
class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
        related_name="pedidos"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def identificador(self):
        return f"ID_{self.id:03d}_Detalle_pedido"

    def __str__(self):
        return self.identificador


# DETALLE_PEDIDO
class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, 
        on_delete=models.CASCADE, 
        related_name="detalles"
    )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
