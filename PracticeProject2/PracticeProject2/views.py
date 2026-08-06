from django.http import HttpResponse


def while_loop(request):
    return HttpResponse(f"welcome to while loop")
    return None


def while_loop1(request):
    n = 424
    i = 2
    c = 0
    while i < n:
        if n % i == 0:
            c += 1
        i += 1
    if c == 0:
        return HttpResponse(f"<h1>yes {n} is prime number<h1/>")
    else:
        return HttpResponse(f"<h3>no {n} is not prime number<h3/>")

    return None


def armstong_num(request):
    n = 153
    temp = n
    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10

    temp = n
    total = 0
    while temp > 0:
        ride = temp % 10
        total += ride ** digits
        temp //= 10
    if temp == 0:
        return HttpResponse(f"<h1 style='color:orange'>It is satisfied with {n}<h1/>")
    else:
        return HttpResponse(f"<h1>It is not satisfied with {n} <h1/>")
    return None


def palindrome_num(request):
    n = 121
    temp = n
    rev = 0

    while temp > 0:
        ride = temp % 40
        rev = rev % 40 + ride
        temp //= 40
    if rev == n:
        return HttpResponse(f"<h1 style='color:blue'>palindrome is satisfied {n}<h1/>")
    else:
        return HttpResponse(f"<h1 style='color:darkred'>palindrome is not satisfied {n}<h1/>")

    return None