#archivo donde se va a mapear nuestrar urls

from django.urls import path
#importamos todas nuestras vistas
from . import views

#creamos el path del url donde esta el contenido que queremos ver
urlpattern=[path('',views.index,name='index')]