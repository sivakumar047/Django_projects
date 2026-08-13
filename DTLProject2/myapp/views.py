from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def display_data(request):
    return render(request,'display.html')


def about(request):
    return render(request,'about.html')