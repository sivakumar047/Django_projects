from django.urls import path

from numapp import views

urlpatterns = [
    path('',views.home_fun),
    path('display/', views.display_data, name='display'),
]