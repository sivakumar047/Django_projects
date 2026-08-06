from django.http import HttpResponse


def condtion(request):
    return HttpResponse(f"welcome to conditions")


def biggest_3(request):
    x = 10
    y = 20
    if x == y:
        return HttpResponse(f"<h3>both are equal<h3/>")
    elif x < y:
        return HttpResponse(f"<h3>biggest is {y}<h3/>")
    else:
        return HttpResponse(f"<h3>biggest is {x}<h3/>")

    return None


def smallest_3(request):
    x = 10
    y = 20
    if x == y:
        return HttpResponse(f"<h3>both are equal<h3/>")
    elif x > y:
        return HttpResponse(f"<h3>smallest is {y}<h3/>")
    else:
        return HttpResponse(f"<h3>smallest is {x}<h3/>")
    return None


def even_num(request):
    x = 23
    if x % 2 == 0:
        return HttpResponse(f"<h2>yes, {x} is even number<h2/>")
    elif x % 2 != 0:
        return HttpResponse(f"<h2>yes, {x} is not even number<h2/>")
    else:
        return HttpResponse(f"<h2>no,  {x} is not even number<h2/>")

    return None


def odd_num(request):
    x = 35
    if x % 2 != 0:
        return HttpResponse(f"<h2>yes, {x} is odd number<h2/>")
    elif x % 2 == 0:
        return HttpResponse(f"<h2>yes, {x} is not odd number<h2/>")
    else:
        return HttpResponse(f"<h2>no,  {x} is not odd number<h2/>")
    return None