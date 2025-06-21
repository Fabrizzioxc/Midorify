from django.shortcuts import render, redirect
from .models import Usuario, Planta, CuidadoProgramado, HistorialAccion, Notificacion
from .forms import PlantaForm
from .supabase_client import subir_imagen
from django.shortcuts import get_object_or_404, redirect, render



from django.views.decorators.http import require_POST

def plantas_list(request):
    if request.method == "POST":
        form = PlantaForm(request.POST, request.FILES)
        if form.is_valid():
            planta = form.save(commit=False)
            planta.usuario = Usuario.objects.first()  # cambia luego por el usuario autenticado

            if 'imagen' in request.FILES:
                try:
                    url = subir_imagen(request.FILES['imagen'])
                    print("🌿 Imagen subida correctamente:", url)
                    planta.foto_url = url
                    print("🔗 URL que se guardará en DB:", planta.foto_url)  # ✅ Aquí sí se ejecutará
                except Exception as e:
                    print("❌ Error al subir imagen:", e)

            planta.save()
            print("✅ Planta guardada:", planta.planta_nom)
            return redirect('plantas-list')

    plantas = Planta.objects.select_related('usuario').all()
    return render(request, 'huerto_app/plantas_list.html', {'plantas': plantas})

def index(request):
    total_plantas = Planta.objects.count()
    total_cuidados = CuidadoProgramado.objects.count()
    total_notificaciones = Notificacion.objects.filter(enviado=False).count()

    return render(request, 'huerto_app/index.html', {
        'total_plantas': total_plantas,
        'total_cuidados': total_cuidados,
        'total_notificaciones': total_notificaciones
    })


def agregar_planta(request):
    if request.method == "POST":
        form = PlantaForm(request.POST, request.FILES)
        if form.is_valid():
            planta = form.save(commit=False)
            planta.usuario = Usuario.objects.first()

            if 'imagen' in request.FILES:
                try:
                    planta.foto_url = subir_imagen(request.FILES['imagen'])
                except Exception as e:
                    print("❌ Error al subir imagen:", e)

            planta.save()
            return redirect('plantas-list')
    else:
        form = PlantaForm()

    return render(request, 'huerto_app/agregar_planta.html', {'form': form})


def editar_planta(request, planta_id):
    planta = get_object_or_404(Planta, planta_id=planta_id)
    
    if request.method == "POST":
        planta.planta_nom = request.POST.get("planta_nom")
        planta.tipo_planta = request.POST.get("tipo_planta")
        planta.cuidados = request.POST.get("cuidados")

        if 'imagen' in request.FILES:
            imagen = request.FILES['imagen']
            try:
                url = subir_imagen(imagen)
                planta.foto_url = url
                print("✅ Imagen subida a Supabase:", url)
            except Exception as e:
                print("❌ Error al subir imagen:", e)

        planta.save()
        return redirect('plantas-list')



@require_POST
def eliminar_planta(request, planta_id):
    planta = get_object_or_404(Planta, planta_id=planta_id)
    planta.delete()
    return redirect('plantas-list')




def cuidados_programados(request):
    cuidados = CuidadoProgramado.objects.select_related("planta").all()
    plantas = Planta.objects.all()
    return render(request, "huerto_app/cuidados_list.html", {"cuidados": cuidados, "plantas": plantas})

@require_POST
def agregar_cuidado(request):
    planta_id = request.POST.get("planta_id")
    tipo = request.POST.get("tipo_cuidado")
    dias = request.POST.get("frecuen_dias")
    fecha = request.POST.get("prox_fecha")
    detalles = request.POST.get("detalles", "")

    planta = Planta.objects.get(pk=planta_id)
    CuidadoProgramado.objects.create(
        planta=planta,
        tipo_cuidado=tipo,
        frecuen_dias=dias,
        prox_fecha=fecha,
        detalles=detalles
    )
    return redirect("cuidados_programados")

@require_POST
def eliminar_cuidado(request, cuidado_id):
    cuidado = get_object_or_404(CuidadoProgramado, pk=cuidado_id)
    cuidado.delete()
    return redirect("cuidados_programados")
