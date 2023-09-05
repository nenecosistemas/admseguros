from django.contrib import admin
from .models import Compania, Iva, Asegurado, Seccion, Poliza

# Register your models here.

admin.site.register(Compania)
admin.site.register(Iva)
admin.site.register(Asegurado)
admin.site.register(Seccion)
admin.site.register(Poliza)