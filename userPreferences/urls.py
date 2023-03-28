from django.contrib import admin
from django.urls import path,include
from userPreferences import views

urlpatterns = [
    path("", views.preferences, name='home-preferences'),
    path("create", views.createPreference, name='create-preferences'),
    path("delete/<int:id>", views.excludePreference, name='exclude-preferences'),
    ]