from django.urls import path

from oddapp import views

urlpatterns = [
    path('oddapp/',views.odd),
    path('oddlist/',views.oddlist)
]