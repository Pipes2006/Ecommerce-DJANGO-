from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.filter(stock__gt=0)
    return render(request, 'tienda/index.html', {'productos': productos})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos': productos})

def carrito(request):
    return render(request, 'tienda/carrito.html')

from .models import Pago
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def pago(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        apellidos = data.get('apellidos')
        email = data.get('email')
        telefono = data.get('telefono')
        direccion = data.get('direccion')
        carrito = data.get('carrito')
        total = data.get('total')
        pago = Pago.objects.create(
            nombre=nombre,
            apellidos=apellidos,
            email=email,
            telefono=telefono,
            direccion=direccion,
            carrito=json.dumps(carrito),
            total=total
        )
        # Crear o actualizar cliente
        from .models import Cliente, Pedido, DetallePedido, Producto
        cliente, created = Cliente.objects.get_or_create(
            email=email,
            defaults={
                'nombre': nombre,
                'apellido': apellidos,
                'telefono': telefono,
                'direccion': direccion
            }
        )
        if not created:
            # Actualizar datos si el cliente ya existía
            cliente.nombre = nombre
            cliente.apellido = apellidos
            cliente.telefono = telefono
            cliente.direccion = direccion
            cliente.save()
        # Crear pedido
        pedido = Pedido.objects.create(
            cliente=cliente,
            total=total
        )
        # Crear detalles del pedido
        for item in carrito:
            try:
                producto = Producto.objects.get(pk=item['id'])
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=int(item['cantidad']),
                    precio_unitario=producto.precio
                )
            except Producto.DoesNotExist:
                pass
        return JsonResponse({'success': True, 'pago_id': pago.id})
    return render(request, 'tienda/pago.html')
