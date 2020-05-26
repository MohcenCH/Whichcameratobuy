from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
#from .filters import OrderFilter


def home(request):


    context = {}
    return render(request, 'Cam/main.html', context)