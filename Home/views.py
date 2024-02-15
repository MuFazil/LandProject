from django.shortcuts import render
from .models import Property

# Create your views here.

def home(request):
    return render(request,'home/my_home.html')


def landing(request):
    p = Property.objects.all()
    return render(request,'home/landing.html',{'p': p})


def detailed_view(request):
    return render(request,'home/detailed_view.html')