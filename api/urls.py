#importamos las funciones de Django, los módulos y las vistas de nuestra aplicación
from django.urls import path, include 
from rest_framework import routers
from api import views

#Creamos una instancia del router por defecto de Django, registramos una ruta específica para el modelo
#bajo el prefijo 'companies' e incluímos todas las rutas registradas en el router en la raiz de la aplicación
router=routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls))
]