from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.home_fun),
    path('onepage/',views.one_fun)
]