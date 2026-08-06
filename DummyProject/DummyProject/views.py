from django.http import HttpResponse


def prac_first(request):
    return HttpResponse(f"welcome to Django practice")


def prac_secon(request):
    return HttpResponse(f"<h3>welcome to html class<h3/>")


def prac_three(request):
    return HttpResponse(f"<h1 style='color:green'>welcome to css class<h1/>")