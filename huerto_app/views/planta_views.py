from django.shortcuts import render, redirect, get_object_or_404
from ..models import Planta, Usuario
from ..forms import PlantaForm
from ..supabase_client import subir_imagen
from django.views.decorators.http import require_POST
from django.http import HttpResponseBadRequest

def plantas_list(request):
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
    plantas = Planta.objects.select_related('usuario').all()
    return render(request, 'huerto_app/plantas_list.html', {'plantas': plantas})


@require_POST
def agregar_planta(request):
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
        return redirect('plantas-list')  # o redirige donde desees
    return HttpResponseBadRequest("Formulario no válido")


def editar_planta(request, planta_id):
    planta = get_object_or_404(Planta, planta_id=planta_id)
    if request.method == "POST":
        planta.planta_nom = request.POST.get("planta_nom")
        planta.tipo_planta = request.POST.get("tipo_planta")
        planta.cuidados = request.POST.get("cuidados")
        if 'imagen' in request.FILES:
            try:
                planta.foto_url = subir_imagen(request.FILES['imagen'])
            except Exception as e:
                print("❌ Error al subir imagen:", e)
        planta.save()
        return redirect('plantas-list')

@require_POST
def eliminar_planta(request, planta_id):
    planta = get_object_or_404(Planta, planta_id=planta_id)
    planta.delete()
    return redirect('plantas-list')
