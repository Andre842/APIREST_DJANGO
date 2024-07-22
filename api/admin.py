from django.contrib import admin #importamos el módulo admin de Django
from .models import Company #importamos el modelo company desde el archivo models.py

#registramos el modelo 'company' en el sitio de administración de Django, para gestionar este modelo
#desde la interfaz de administración de Django
admin.site.register(Company)