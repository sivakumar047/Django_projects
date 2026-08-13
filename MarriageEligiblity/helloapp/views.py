from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_fun(request):
    if request.method == "POST":

        age = int(request.POST.get("age"))
        gender = request.POST.get("gender")

        if gender == "male" and age >= 21:
            result = "eligible"

        elif gender == "female" and age >= 18:
            result = "eligible"

        else:
            result = "not eligible"

        return render(request, "home.html", {
            "age": age,
            "gender": gender,
            "result": result
        })

    return render(request, "home.html")