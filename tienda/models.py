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
class MetodoPago(models.Model):
    tipo_pago = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_pago


# PEDIDO
class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
        related_name="pedidos"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    metodo_pago = models.ForeignKey(
        MetodoPago, 
        on_delete=models.SET_NULL, 
        null=True
    )

    def __str__(self):
        return f"Pedido {self.id} - Cliente {self.cliente}"


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
