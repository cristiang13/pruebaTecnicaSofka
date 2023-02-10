from django.db import models

# Create your models here.
class VehiculoEspacial(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)   
    nombre = models.CharField(max_length=100)
    tipo_propulsion = models.CharField(max_length=100)
    capacidad_transporte = models.FloatField()
    peso = models.FloatField()
    empuje = models.FloatField()
    
    class Meta:
        abstract = True
    

class VehiculoLanzadera(VehiculoEspacial):
    altura = models.FloatField()

class VehiculoNoTripulado(VehiculoEspacial):
       pass

class VehiculoTripulado(VehiculoEspacial):
    orbita = models.CharField(max_length=100)



# class Nave(models.Model):
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()
#     tipo = models.CharField(max_length=100)
#     peso = models.CharField(max_length=100)
#     empuje = models.CharField(max_length=100)
#     caracteristicas = models.TextField()
    
#     def __str__(self):
#         return self.nombre