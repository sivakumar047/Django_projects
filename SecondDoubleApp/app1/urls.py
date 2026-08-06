from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.home_fun),
    path('json/',views.json_fun)
]