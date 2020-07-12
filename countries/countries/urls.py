from django.contrib import admin
from django.urls import path
from city_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.addCount),
    path('delete/<int:id>/', views.delete),
    path('create-city/', views.addCity),
    path('update/<int:id>/', views.update),
    path('update/<int:id>/update-country/', views.updateCountry),
    path('update/<int:id>/delete-city/', views.deleteCity),
    path('', views.index)
]