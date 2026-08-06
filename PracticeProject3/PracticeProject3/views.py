from django.http import HttpResponse
x = [10,11,12,13,15,17,14,16,18,20,19]

def num_for(request):
    return HttpResponse(f"Welcome to for loops")


def even_num(request):
    even_num1 = []
    for i in x:
        if i % 2 == 0:
            even_num1.append(i)
    return HttpResponse(f"<h1 style='color:red'>It is even number<h1/>")

    return None


def odd_num(request):
    odd_num1 = []
    for i in x:
        if i % 2 != 0:
            odd_num1.append(i)
    return HttpResponse(f"<h1 style='color:Brown'>It is not even number<h1/>")
    return None


def even_num_index(request):
    even_num_index1 = []
    for i in range(len(x)):
        if i % 2 == 0:
            even_num_index1.append(i)
    return HttpResponse(f"<h1 style='color:Green'>It is showing even_num_index1<h1/>")

    return None


def odd_num_index(request):
    odd_num_index1 = []
    for i in range(len(x)):
        if i % 2 != 0:
            odd_num_index1.append(i)
    return HttpResponse(f"<h1 style='color:purple'>It is showing odd_num<h1/>")
    return None