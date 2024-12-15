""" ------------------Importamos clases de django------------------"""
from django.urls import path
from .views import Mensajes,Nombre

""" ------------------Creamos el array con distintos endpoints---------------- """
urlpatterns = [
    path('hola/',Mensajes.as_view(),name='holamundo'),
    path('hola/<str:nombre>',Nombre.as_view(),name='holaparametro') # Con esta url podemos recibir un parametro
]