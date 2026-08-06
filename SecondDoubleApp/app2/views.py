from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_fun(request):
    return HttpResponse("welcome to app2!")


def even_odd_fun(request,num):
    if num%2==0 and num > 0 :
        return HttpResponse(f'given number is even')
    elif num % 2 == 1 and num > 0:
        return HttpResponse(f'given number is odd')
    elif num == 0:
        return HttpResponse(f'given number is zero')
    else:
        return HttpResponse(f'given number is negative')
    
    return None