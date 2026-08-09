from django.shortcuts import render

# Create your views here.
def home_fun(request):
    return render(request,'leap.html')

def leap(request):
    result = ""

    if request.method == "POST":
        year = int(request.POST['year'])

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            result = "Leap year"
        else:
            result = "Not a leap year"

    return render(request, 'leap.html', {'result': result})


def marriage(request):
    result = ""

    if request.method == "POST":
        age = int(request.POST['age'])
        gender = request.POST['gender']

        if (gender == "male" and age >= 21) or (gender == "female" and age >= 18):
            result = "Eligible"
        else:
            result = "Not Eligible"

    return render(request, 'marriage.html', {'result': result})