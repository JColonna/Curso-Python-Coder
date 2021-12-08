#Este lo creo yo para darle la url a la vista
from django.urls import path
from Appcoder import views


urlpatterns = [
   
    path('inicio', views.inicio),
    path('jugadores', views.jugadores),
    
]
