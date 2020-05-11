from django.shortcuts import render, HttpResponse
import json
from .models import Vino, Bodega

# Create your views here.


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def register(request):
    return render(request, "core/register.html")


def carrito(request):
    return render(request, "core/carrito.html")


def productos(request):
    return render(request, "core/productos.html")


def login(request):
    return render(request, "core/login.html")


def producto(request):
    return render(request, "core/producto.html")


def proyecto(request):
    return render(request, "core/proyecto.html")
