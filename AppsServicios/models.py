from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#servicios que ofrecemos

class Servicios(models.Model):
    nombre = models.CharField(max_length=128)
    tiempo=models.CharField(max_length=128)
    valor = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}"

# nombre de las tecnologias

class Tecnologias(models.Model):
   nombre = models.CharField(max_length=128)
   version = models.CharField(max_length=128)
   
   def __str__ (self):
      return f"{self.nombre}"

#nombre de contactos
class Contactos(models.Model):
   nombre = models.CharField(max_length=128)
   apellido = models.CharField(max_length=128)
   email = models.EmailField()
   
   #Se usa para ver la info de SQL en admin

   def __str__(self):
      return f"{self.apellido}, {self.nombre}"

#class Avatar(models.Model):
    # Vinculo con el usuario
 #   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
  #  imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

   # def __str__(self):
    #    return f"Imagen de: {self.user}"