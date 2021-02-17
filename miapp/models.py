from django.db import models

# Create your models here.
class Region(models.Model):
    date = models.CharField(max_length=20, verbose_name="Date")
    name= models.CharField(max_length=20, verbose_name="Name")
    cases = models.CharField(max_length=2, verbose_name="Cases")
    deaths = models.CharField(max_length= 12, verbose_name="Deaths")
    lethality = models.CharField(max_length= 1, verbose_name="Lethality")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Editado")
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Region"
        ordering = ['name']
    ##mostrar letras mejores al momento de observar en la tabla de control principal