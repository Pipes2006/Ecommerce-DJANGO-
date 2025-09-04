from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Importar settings
from django.conf.urls.static import static  # Importar static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),  # Esto incluye las URLs de tu app tienda
]

# Agregar configuración para servir archivos estáticos y medios en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)