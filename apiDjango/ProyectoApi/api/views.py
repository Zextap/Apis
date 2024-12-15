"""-----------------Importar clases de django--------------------- """
from django.views import View  # Clase para manejar las vistas
from django.http.response import JsonResponse # Clase para manejar las respuestas en Json
# Create your views here.

""" ----------------Clases que devuelven el mensaje de un endpoint----------- """
class Mensajes (View):
    def get(response,request):
        mensaje = {"mensaje" : "hola mundo"} # Mensaje en formato Json
        return JsonResponse(mensaje)

class Nombre (View):
    def get(res,req,nombre): # Añadimos un parametro que recibirar de la url
        menaje = {"mensaje":"hola "+nombre}
        return JsonResponse(menaje)