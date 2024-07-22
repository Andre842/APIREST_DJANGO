from django.db import models #importamos el módulo models de Django

# Creamos los modelos

#Definimos un modelo llamado 'company' que hereda de models.Model y luego creamos los campos para este modelo
class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField()