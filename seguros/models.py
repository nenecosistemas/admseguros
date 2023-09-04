from django.db import models

# Create your models here.

class compania(models.Model):
  cuit_compania=models.CharField(primary_key=true,max_length=15)
  nombre_compania=models.CharField(max_length=255) 
  tipoiva_compania=models.PositiveSmallIntengerField() 
  domicilio_compania=models.CharField(max_length=255) 
  telefono_compania=models.CharField(max_length=45) 
  correo_compania=models.Charfield(max_length=45)

  def __str__(self):
    texto = "{0} ({1})"
    return texto.format(self.nombre_compania, self.cuit_compania)
