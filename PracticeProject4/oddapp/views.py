from django.http import HttpResponse
numbers = [10,11,12,13,15,17,14,16,18,20,19]

def odd(request):
    odd = []

    for i in numbers:
        if i % 2 != 0:
            odd.append(i)
    return HttpResponse(f"<h1>This is an odd<h1/>")
    return None


def oddlist(request):
    total = 0

    for i in numbers:
        if i % 2 != 0:
            total += i
    return HttpResponse(f"<h1>This is an oddlist<h1/>")
    return None