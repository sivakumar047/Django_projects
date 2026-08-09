from django.urls import path

from app2 import views

urlpatterns = [
    path('', views.leap, name='leap'),
    path('marriage/', views.marriage, name='marriage'),
]