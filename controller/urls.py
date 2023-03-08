from django.contrib import admin
from django.urls import path,include
from controller import views

urlpatterns = [
    path('home',views.home,name='controller_home')
    ]
