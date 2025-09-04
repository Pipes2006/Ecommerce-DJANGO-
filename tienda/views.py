from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/index.html', {'productos': productos})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos': productos})

def carrito(request):
    return render(request, 'tienda/carrito.html')
