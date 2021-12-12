#Este lo creo yo para darle la url a la vista
from django.urls import path
from Appcoder import views


urlpatterns = [
   
    path('inicio', views.inicio, name = "Inicio"),
    path('jugadores', views.jugadores, name = "Jugadores"),
    
    
]
