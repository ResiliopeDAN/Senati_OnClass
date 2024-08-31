from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota

# Create your views here.

def index(request):
    mascotas = Mascota.objects.all
    context = {'mascotas':mascotas}

    return render(request,'adopcion/index.html', context)