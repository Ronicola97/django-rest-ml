from django.db import models

# Create your models here.
class Diagnostico(models.Model):
    enfermedad = models.CharField(max_length = 200)
    porcentaje = models.FloatField()
    ficha = models.IntegerField()
    fecha_analisis = models.DateTimeField(auto_now_add=True)
