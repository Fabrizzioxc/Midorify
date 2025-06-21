from django.urls import path
from huerto_app.views.dashboard_views import index
from huerto_app.views.planta_views import plantas_list, agregar_planta, editar_planta, eliminar_planta
from huerto_app.views.cuidado_views import cuidados_programados, agregar_cuidado, eliminar_cuidado
from .views import cuidado_views as views

urlpatterns = [
    path('', index, name='index'),

    # Plantas
    path('plantas/', plantas_list, name='plantas-list'),
    path('plantas/nueva/', agregar_planta, name='planta-nueva'),
    path('editar_planta/<int:planta_id>/', editar_planta, name='editar_planta'),
    path('eliminar_planta/<int:planta_id>/', eliminar_planta, name='eliminar_planta'),

    # Cuidados
    path("cuidados/", cuidados_programados, name="cuidados_programados"),
    path("cuidados/agregar/", agregar_cuidado, name="agregar_cuidado"),
    path("cuidados/eliminar/<int:cuidado_id>/", eliminar_cuidado, name="eliminar_cuidado"),
    path('cuidados/editar/<int:cuidado_id>/', views.editar_cuidado, name='editar_cuidado'),
]
