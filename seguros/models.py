from django.db import models

# Create your models here.
class Iva(models.Model):  
  nombre_iva=models.CharField(max_length=45) 
  descripcion_iva=models.CharField(max_length=255)   
  def __str__(self):
    texto = "{0} - {1}"
    return texto.format(self.nombre_iva,self.descripcion_iva)  
  class Meta:
        ordering = ['descripcion_iva']

class Compania(models.Model):
  cuit_compania=models.CharField(primary_key=True,max_length=15)
  nombre_compania=models.CharField(max_length=255) 
  tipoiva_compania=models.ForeignKey(Iva, on_delete=models.PROTECT)
  domicilio_compania=models.CharField(max_length=255,blank=True) 
  telefono_compania=models.CharField(max_length=45,blank=True) 
  correo_compania=models.CharField(max_length=45,blank=True)

  def __str__(self):
    texto = "{0} ({1})"
    return texto.format(self.nombre_compania, self.cuit_compania)
  class Meta:
        ordering = ['nombre_compania']

class Asegurado(models.Model):
  dni_asegurado=models.CharField(verbose_name="D.N.I:", primary_key=True, max_length=15)
  apellido_y_nombre_asegurado=models.CharField(verbose_name="Apellido y Nombre:",max_length=255)
  domicilio_asegurado=models.CharField(verbose_name="Domicilio:",max_length=255, blank=True)
  telefono_asegurado=models.CharField(verbose_name="Teléfono:",max_length=45, blank=True)
  correo_asegurado=models.CharField(verbose_name="Correo Electrónico:",max_length=45, blank=True)
  tipoiva_asegurado=models.ForeignKey(Iva,on_delete=models.PROTECT,verbose_name="Tipo IVA:")
  cuit_asegurado=models.CharField(verbose_name="C.U.I.T.:",max_length=45, blank=True)
  def __str__(self):
    texto = "{0} ({1})"
    return texto.format(self.apellido_y_nombre_asegurado, self.dni_asegurado)
  class Meta:
        ordering = ['apellido_y_nombre_asegurado']
        
class Seccion(models.Model):
  nombre_seccion=models.CharField(max_length=45)        
  descripcion_seccion=models.CharField(max_length=255)
  def __str__(self):
    texto = "{0} - ({1})"
    return texto.format(self.nombre_seccion, self.descripcion_seccion)
  class Meta:
        ordering = ['nombre_seccion']
        verbose_name_plural = 'Secciones'
        
class Poliza(models.Model):
  compania = models.ForeignKey("Compania", on_delete=models.PROTECT)
  seccion = models.ForeignKey("Seccion", on_delete=models.PROTECT)
  asegurado = models.ForeignKey("Asegurado", on_delete=models.PROTECT)  
  poliza_nro=models.CharField(max_length=45)
  endoso_nro=models.CharField(max_length=45)
  renovacion_poliza=models.CharField(max_length=45,blank=True)
  fecha_emision=models.DateField(blank=True,null=True)
  vigencia_desde=models.DateField(blank=True,null=True)
  vigencia_hasta=models.DateField(blank=True,null=True)
  descripcion_asegurado=models.CharField(max_length=255)
  cobertura_asegurado=models.CharField(max_length=255)
  suma_asegurada=models.CharField(max_length=45)
  prima=models.CharField(max_length=45)
  premio=models.CharField(max_length=45)
  def __str__(self):
    texto = "Poliza: {0} - {1} - {2}"        
    return texto.format(self.poliza_nro, str(self.fecha_emision) , self.asegurado)
  class Meta:
        ordering = ['poliza_nro']
        
  
  
