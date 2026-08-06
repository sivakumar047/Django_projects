"""
URL configuration for PracticeProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from PracticeProject1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.condtion),
    path('biggest/',views.biggest_3),
    path('smallest/',views.smallest_3),
    path('even/',views.even_num),
    path('odd/',views.odd_num)
]
