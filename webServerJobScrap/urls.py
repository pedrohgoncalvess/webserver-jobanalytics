from django.contrib import admin
from django.urls import path,include
from webServerJobScrap import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('controller/',include('controller.urls')),
    path("",views.home,name='home')
]
