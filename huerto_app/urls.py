from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  

    
    path('plantas/', views.plantas_list, name='plantas-list'),
    path('plantas/nueva/', views.agregar_planta, name='planta-nueva'),
    path('editar_planta/<int:planta_id>/', views.editar_planta, name='editar_planta'),
    path('eliminar_planta/<int:planta_id>/', views.eliminar_planta, name='eliminar_planta'),


    path("cuidados/", views.cuidados_programados, name="cuidados_programados"),
    path("cuidados/agregar/", views.agregar_cuidado, name="agregar_cuidado"),
    path("cuidados/eliminar/<int:cuidado_id>/", views.eliminar_cuidado, name="eliminar_cuidado"),

]
