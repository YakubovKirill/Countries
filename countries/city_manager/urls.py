from django.contrib import admin
from django.urls import path, url
from city_manager import views
#from city_manager.models import *

urlpatterns = [
    path('/admin', admin.site.urls),
    path('/create', views.addCount),
    path('', views.index)
]