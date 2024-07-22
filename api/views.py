#importamos los módulos, modelos y serializadores
from rest_framework import viewsets
from .models import Company
from .serializer import CompanySerializer


#Definimos un conjunto de vistas que hereda de viewsets.ModelViewSet
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all() #definimos el queryset que retorna todos los objetos del modelo 'company'
    serializer_class = CompanySerializer #especificamos el serializador a utilizar


