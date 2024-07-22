#convertir los datos nativos a un json
from rest_framework import serializers #importamos el módulo serializers de Django REST framework
from .models import Company #importamos el modelo company

#Definimos un serializador que hereda de serializers.ModelSerializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta: #esta clase interna proporciona información sobre el modelo
        model = Company #especificamos el modelo
        fields = '__all__' #incluímos todos los campos de este modelo en el serializador
