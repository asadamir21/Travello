from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    destinations = Destination.objects.all()

    return render(request, "index.html", {'destinations': destinations})
