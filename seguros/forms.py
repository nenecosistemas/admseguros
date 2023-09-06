from django.forms import ModelForm
from .models import *

class AseguradoForm(ModelForm):
    class Meta:
        model = Asegurado
        fields = '__all__'