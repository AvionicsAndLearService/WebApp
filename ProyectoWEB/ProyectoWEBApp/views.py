from django.shortcuts import render, HttpResponse
from basedatos.models import ot 
# Create your views here.

def Home(request):
    return render(request, "ProyectoWEBApp/Inicio.html")

def Admin(request):
    return render(request, "ProyectoWEBApp/admin.html")

def OT(request):
    ordenes=ot.objects.all()
    return render(request, "ProyectoWEBApp/ot.html", {"ordenes": ordenes})

def Almacen(request):
    return render(request, "ProyectoWEBApp/almacen.html")

def Blog(request):
    return render(request, "ProyectoWEBApp/blog.html")