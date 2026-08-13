from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.home_fun),
    path('about/',views.about_fun,name='about')
]