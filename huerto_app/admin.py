from django.contrib import admin
from .models import Usuario, Planta, CuidadoProgramado, HistorialAccion, Notificacion

admin.site.register(Usuario)
admin.site.register(Planta)
admin.site.register(CuidadoProgramado)
admin.site.register(HistorialAccion)
admin.site.register(Notificacion)
