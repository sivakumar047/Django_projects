from django.http import HttpResponse


def home_fun(request):
    return HttpResponse(f"welcome to urls page")


def one_fun(request):
    return HttpResponse(f"welcome to page 1 urls")
