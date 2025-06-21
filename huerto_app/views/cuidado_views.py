from django.shortcuts import render, redirect, get_object_or_404
from ..models import CuidadoProgramado, Planta
from django.views.decorators.http import require_POST
from django.contrib import messages

def cuidados_programados(request):
    cuidados = CuidadoProgramado.objects.select_related("planta").all()
    plantas = Planta.objects.all()
    return render(request, "huerto_app/cuidados_list.html", {"cuidados": cuidados, "plantas": plantas})

@require_POST
def agregar_cuidado(request):
    planta = Planta.objects.get(pk=request.POST.get("planta_id"))
    CuidadoProgramado.objects.create(
        planta=planta,
        tipo_cuidado=request.POST.get("tipo_cuidado"),
        frecuen_dias=request.POST.get("frecuen_dias"),
        prox_fecha=request.POST.get("prox_fecha"),
        hora = request.POST.get("hora"),
        detalles=request.POST.get("detalles", "")
    )
    return redirect("cuidados_programados")

@require_POST
def eliminar_cuidado(request, cuidado_id):
    cuidado = get_object_or_404(CuidadoProgramado, pk=cuidado_id)
    cuidado.delete()
    return redirect("cuidados_programados")

@require_POST
def editar_cuidado(request, cuidado_id):
    cuidado = get_object_or_404(CuidadoProgramado, pk=cuidado_id)

    # No cambiamos la planta (ya viene oculta en el form y es solo lectura)
    cuidado.tipo_cuidado = request.POST.get('tipo_cuidado')
    cuidado.frecuen_dias = request.POST.get('frecuen_dias')
    cuidado.prox_fecha = request.POST.get('prox_fecha')
    cuidado.hora = request.POST.get('hora') or None
    cuidado.detalles = request.POST.get('detalles') or ""

    cuidado.save()
    messages.success(request, "Cuidado actualizado correctamente.")
    return redirect('cuidados_programados')