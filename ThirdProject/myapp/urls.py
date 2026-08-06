from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.home_fun),
    path('display/',views.display_data)
]