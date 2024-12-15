from django.urls import path
from .views import Mensajes,Nombre

urlpatterns = [
    path('hola/',Mensajes.as_view(),name='holamundo'),
    path('hola/<str:nombre>',Nombre.as_view(),name='holaparametro')
]