from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template import loader

def home(request):
    return render(request, "aplicacion/home.html")

def cursos(request):
    return render(request, 'aplicacion/cursos.html')

def profesores(request):
    return render(request, 'aplicacion/profesores.html')

def estudiantes(request):
    return render(request, 'aplicacion/estudiantes.html')

def entregables(request):
    return render(request, 'aplicacion/entregables.html')
