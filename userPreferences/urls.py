from django.contrib import admin
from django.urls import path,include
from userPreferences import views

urlpatterns = [
    path("", views.preferences, name='preferences'),
    path("create", views.createPreference, name='create-preferences'),
    path("view", views.viewPreferences, name='view-preference'),
    path("delete/<int:id>", views.excludePreference, name='exclude-preferences'),
    path("edit/<int:id>",views.editPreference,name='edit-preference')
    ]