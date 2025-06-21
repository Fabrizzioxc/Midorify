from django.shortcuts import render
from ..models import Planta, CuidadoProgramado, Notificacion

def index(request):
    return render(request, 'huerto_app/index.html', {
        'total_plantas': Planta.objects.count(),
        'total_cuidados': CuidadoProgramado.objects.count(),
        'total_notificaciones': Notificacion.objects.filter(enviado=False).count()
    })
