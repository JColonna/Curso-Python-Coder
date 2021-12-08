from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    
    #return HttpResponse('Esto es una prueba del inicio')
    return render(request, 'Appcoder/inicio.html') #Relaciono con el template

def jugadores(request):
    

    return render(request, 'Appcoder/jugadores.html') #Relaciono con el template