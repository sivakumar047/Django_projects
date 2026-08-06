from django.http import HttpResponse



def home_fun(request):
    return HttpResponse("welcome to Django class")


def html_fun(request):
    return HttpResponse(f"<h1>welcome to Django class</h1>")


def css_fun(request):
    return HttpResponse(f"<h1 style='color:red'>welcome to css class</h1>")