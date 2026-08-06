from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def home_fun(request):
    return HttpResponse("welcome to app1")


def json_fun(request):
    return JsonResponse({"hello":"world",
                         "method":str(request.method),
                         'ip':str(request.META['REMOTE_ADDR']),
                         'path':str(request.path)})