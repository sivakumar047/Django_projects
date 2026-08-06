from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_fun(request):
    return render(request,'home.html')


def display_data(request):
    num1 = int(request.GET.get("num1"))
    num2 = int(request.GET.get("num2"))

    total = num1 + num2

    data = {
        "num1": num1,
        "num2": num2,
        "total": total
    }
    return render(request, 'display.html',data)