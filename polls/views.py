from django.shortcuts import render

# Create your views here.
# cremos una nueva vista. esta vista es algun contenido , ojo no es la URL. AUN SE FALTA MAPEAR LA URL para acceder.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo,  llamado desde polls index")