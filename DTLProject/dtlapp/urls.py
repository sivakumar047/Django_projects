from django.urls import path

from dtlapp import views

urlpatterns = [
    path('',views.home_fun),
]