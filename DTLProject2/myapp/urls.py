from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('display/',views.display_data,name='display'),
    path('about/',views.about,name='about'),
]