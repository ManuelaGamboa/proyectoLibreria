from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
	return render(request, 'index.html')

def novedades(request):
	return render(request, 'novedades.html')

def colecciones(request):
	return render(request, 'colecciones.html')

def promociones(request):
	return render(request, 'promociones.html')