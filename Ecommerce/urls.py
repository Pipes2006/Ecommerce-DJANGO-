
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Importar settings
from django.conf.urls.static import static  # Importar static
from django.http import HttpResponse

def loaderio_verificacion(request):
    return HttpResponse("loaderio-41cd1926282badfe09dabef852901e9e", content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),  # Esto incluye las URLs de la app tienda
    path('loaderio-41cd1926282badfe09dabef852901e9e.txt', loaderio_verificacion),
]

# Agregar configuración para servir archivos estáticos y medios en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)