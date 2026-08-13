from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    name="ramesh"
    products=[{"name":"mobile","price":10000},
              {"name":"laptop","price":50000},
              {"name":"bike","price":80000}]
    numbers=[10,11,12,13,14,15,16,17,18,19,20]
    no1=10
    no2=20
    return render(request,'home.html',{"name":name,
                                       "product":products,
                                       "numbers":numbers,
                                       "no1":no1,"no2":no2})