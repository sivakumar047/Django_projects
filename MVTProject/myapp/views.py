from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_fun(request):
    if request.method == "POST":
        num1=int(request.POST.get("txtnum1"))
        num2=int(request.POST.get("txtnum2"))
        operation=request.POST.get("operation")
        res=""
        if operation=="add":
            res = num1 + num2
        elif operation=="mul":
            res = num1 * num2
        elif operation=='power':
            res = pow(num1,num2)
        return render(request,'home.html',{'no1':num1,
                                           'no2':num2,
                                           'res':res})

    return render(request,'home.html')


def about_fun(request):
    return HttpResponse("hello world")