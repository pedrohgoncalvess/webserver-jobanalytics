from django.shortcuts import render, redirect

def home(request):
    return render(request, 'controller/home_controller.html')