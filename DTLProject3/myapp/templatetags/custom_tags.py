from django import template

register = template.Library()

@register.simple_tag
def make_upper(name):
    return name.upper()
@register.simple_tag
def greet(name):
    return f"hello {name}"
@register.simple_tag
def custom_tag_fun():
    return f"hello welcome to custom tags "
@register.simple_tag
def add_fun(n1,n2):
    return n1 + n2

@register.filter
def list_sum(list_1):
    return sum(list_1)
@register.filter
def even_index_even_sum(list_1):
    sum1 = 0
    for i in range(0,len(list_1)):
        if list_1[i] % 2 == 0:
            sum1 += list_1[i]
    return sum1


