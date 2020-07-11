from django.contrib import admin
from django.urls import path
from city_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.addCount),
    path('create-city/', views.addCity),
    path('', views.index)
]