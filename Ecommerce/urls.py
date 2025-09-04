from django.contrib import admin
from django.urls import path
from django.conf import settings  # Importar settings
from django.conf.urls.static import static  # Importar static
from tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]

# Agregar configuración para servir archivos estáticos y medios en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)