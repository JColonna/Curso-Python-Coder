from django import http
from django.http import HttpResponse
from datetime import date, datetime
from django.template import Template, Context   
#Paso 1 simplificar  la relacion del template y el views.py
from django.template import loader 
def saludo (request):
    return HttpResponse('Hola Django -- Primer vista')

def index(request):
    return HttpResponse('----Ya somos programadores----')

def dia(request):
    var = datetime.now()
    return HttpResponse(f'Hoy es un gran dia <br> {var}')

def apellido(request, ape):
    fecha = datetime.now()
    return HttpResponse(f'El profe de coder {ape} es muy bueno ... <br><br> Por lo menos hoy {fecha}')

def edad(request, añoNac):
    
    return HttpResponse(f'Nacio en el año {añoNac}')

def template(request):
    #Declaro variables para enviar al html, creando un diccionario y enviandolo al contexto

    mejorEstudiante = 'Joaquin'
    nota = 10
    fecha = datetime.now()
    estudiantesMasSimpaticos = ['Juance', 'Nadia', 'Victor', 'Laura']
    dic = {'nombre' : mejorEstudiante, 'nota' : nota, 'fecha' : fecha, 'estudiantes' : estudiantesMasSimpaticos}
   
    #Para reemplazar todo el choclo de abajo
    #1 pego ruta en settings template dir y borro el archivo
    #2 cargo en la vista
    plantilla = loader.get_template('template1.html')
    #3 renderizo
    documento = plantilla.render(dic)
    return HttpResponse(documento)

    #Abrir documento
    #miHTML = open("C:/Users/joaqu/OneDrive/Documentos/Python/Proyectos/Proyecto1/Proyecto1/plantillas/template1.html")
    #Cargar en la memoria el documento
    #plantilla = Template(miHTML.read())
    #Cerramos archivo
    #miHTML.close()
    #Defino mi contexto
    #miContexto = Context(dic)
    #Transformar a un contenido web, renderizado
    #documento = plantilla.render(miContexto)
    #Devuelvo documento
    #return HttpResponse(documento)