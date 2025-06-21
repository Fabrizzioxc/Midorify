from django import forms
from .models import Planta

class PlantaForm(forms.ModelForm):
    imagen = forms.FileField(required=False)

    class Meta:
        model = Planta
        fields = ['planta_nom', 'tipo_planta', 'cuidados']
