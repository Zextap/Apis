from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
# Create your views here.

class Mensajes (View):
    def get(response,request):
        mensaje = {"mensaje" : "hola mundo"}
        return JsonResponse(mensaje)

class Nombre (View):
    def get(res,req,nombre):
        menaje = {"mensaje":"hola "+nombre}
        return JsonResponse(menaje)