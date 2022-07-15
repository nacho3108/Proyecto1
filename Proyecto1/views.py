from ast import For
from django import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template


def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):
    dia = datetime.now()
    documentoDeTexto = f"Hoy es día: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: <br> {nombre}"
    return HttpResponse(documentoDeTexto)

def anioNacimiento(self, edad):
    
    currentDateTime = datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    anioNac = int(year) - int(edad)
    documentoDeTexto = f"Usted nació en el año: {anioNac}"
    return HttpResponse(documentoDeTexto)

def probandoTemplate(request):

    miHtml = open(r"C:\Users\ignac\OneDrive\Escritorio\CoderHouse\PythonProyecto1\Proyecto1\Proyecto1\plantillas\template1.html")
    
    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1
    # Ojo importar: from django.template import Template, Context

    miHtml.close() # Cerramos el archivo
    
    miContexto = Context() #En este caso no hay nada ya que no hay parametros, igual hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)

