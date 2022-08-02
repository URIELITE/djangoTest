import imp
from django.shortcuts import render

# Create your views here.

#creamos nuestra primera vista "index html"

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola Mundo , desde POLLS django")