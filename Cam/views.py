from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
#from .filters import OrderFilter


def home(request):

    Products = Product.objects.all()

    context = {"products":Products}
    return render(request, 'Cam/main.html', context)

