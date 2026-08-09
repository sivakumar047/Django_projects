from django.shortcuts import render

# Create your views here.
def home_fun(request):
    x = 10
    y = 20
    names=["ramesh","suresh","poojitha","srinu","veena","reena"]
    students_data=[['akhil''bablu','charan'],[100,95,90]]
    employees_data=[{'name':'riya','age':23},{'name':'teju','age':24}]

    context ={"no1":x,"no2":y,"names":names,"students":students_data,
              "employees":employees_data}


    return render(request,'home.html',context)