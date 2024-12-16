from django.shortcuts import render
from .models import Vehiculo

# Create your views here.

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/lista.html', {'vehiculos': vehiculos})
