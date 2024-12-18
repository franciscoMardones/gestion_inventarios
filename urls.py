from django.contrib import admin
from django.urls import path, include
from inventario.views import home  # Importa la vista de inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('inventario/', include('inventario.urls')),
    path('', home, name='home'),  # Ruta para la página de inicio
]
