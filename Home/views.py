from django.shortcuts import render
from .models import Property

# Create your views here.

def homepage(request):
    return render(request,'home/homepage.html')


def detailed_view(request):
    return render(request,'home/detailed_view.html')

def properties(request):
    return render(request,'home/properties.html')