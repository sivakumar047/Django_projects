from django.urls import path

from evenapp import views

urlpatterns = [
    path('',views.home_fun),
    path('even/',views.even),
    path('evenlist/',views.evenlist),
    path('evensum/',views.evensum),
]