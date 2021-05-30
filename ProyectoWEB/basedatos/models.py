from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, create_many_to_many_intermediary_model

# Create your models here.

class ot(models.Model):
    orden_ALS=models.CharField(max_length=50)
    matricula=models.CharField(max_length=50, null=True, blank=True)
    cliente=models.CharField(max_length=50,null=True, blank=True)
    modelo=models.CharField(max_length=50,null=True, blank=True)
    serie=models.CharField(max_length=20,null=True, blank=True )
    hangar=models.CharField(max_length=20,null=True, blank=True)
    reporte=models.TextField(max_length=5000)
    accion=models.TextField(max_length=50000)
    tecnicos=models.CharField(max_length=20,null=True, blank=True)
    observacion=models.TextField(max_length=5000,null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, blank=True) 
    updated=models.DateTimeField(auto_now_add=True, blank=True)


    class Meta:
        verbose_name='OT'
        verbose_name_plural="OT's"
    
    def __str__(self):
        return self.matricula

class calificacion(models.Model):
    orden= models.ForeignKey(ot, null=False, blank=False, on_delete=models.CASCADE)
    precio=models.CharField(max_length=50)
    
    def __str__(self):
        return self.orden