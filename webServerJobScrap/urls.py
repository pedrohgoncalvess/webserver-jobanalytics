from django.contrib import admin
from django.urls import path,include
from webServerJobScrap import views
from webServerJobScrap.preferences import views as viewpref

urlpatterns = [
    path('admin/', admin.site.urls),
    path('controller/',include('controller.urls')),
    path("",views.home,name='home'),
    path("preferences/",viewpref.preferences,name='preferences'),
    path("preferences/create",viewpref.createPreference,name='create-preferences'),
    path("preferences/view",viewpref.viewPreferences,name='view-preference'),
    path("preferences/delete/<int:id>",viewpref.excludePreference,name='exclude-preferences')
]
