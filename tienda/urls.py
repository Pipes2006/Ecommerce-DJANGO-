from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('carrito/', views.carrito, name='carrito'),
    path('pago/', views.pago, name='pago'),
]
