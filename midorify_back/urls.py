from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas para el frontend
    path('', include('huerto_app.urls')),

]
