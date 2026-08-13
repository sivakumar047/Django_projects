from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_fun(request):
    return render(request, 'home.html')

def display_data(request):
    number = int(request.POST.get('number'))

    return render(request, 'display.html', {
        'number': number
    })
