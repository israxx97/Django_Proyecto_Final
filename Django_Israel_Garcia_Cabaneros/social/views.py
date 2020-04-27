from django.shortcuts import render, HttpResponse
from .models import Social

# Create your views here.


def social(request):
    redes_sociales = Social.objects.all()
    return render(request, "social/social.html", {'redes_sociales': redes_sociales})
