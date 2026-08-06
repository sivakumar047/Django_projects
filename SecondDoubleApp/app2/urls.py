from django.urls import path

from app2 import views

urlpatterns = [
    path('',views.home_fun,name='home'),
    path('even_odd/<int:num>/',views.even_odd_fun)
]