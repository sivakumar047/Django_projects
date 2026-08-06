from django.http import HttpResponse
from django.shortcuts import render
numbers = [10,11,12,13,15,17,14,16,18,20,19]

# Create your views here.
def home_fun(request):
    return HttpResponse("welcome to django")
    return None


def even(request):
    return HttpResponse(f"<h1>This is a even numbers<h1/>")
    return None


def evenlist(request):
    even = []

    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return HttpResponse(f"<h1>This is a evenlist1 number<h1/>")
    return None


def evensum(request):
    total = 0

    for i in numbers:
        if i % 2 == 0:
            total += i
    return HttpResponse(f"<h1>This is a even sum number<h1/>")
    return None


def oddlist(request):
    odd = []

    for i in numbers:
        if i % 2 != 0:
            odd.append(i)
    return HttpResponse(f"<h1>This is a oddlist<h1/>")
    return None