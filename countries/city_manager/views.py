from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# main page view

def index(request):
    countries = Country.objects.all()
    cities = City.objects.all()
    return render(request, "city_manager/index.html", {
        "countries": countries,
        "cities": cities
    })

# Add country to database
def addCount(request):
    if request.method == "POST":
        count = Country()
        count.country_name = request.POST.get("country")
        count.save()
    return HttpResponseRedirect("/")

# Add city to database
def addCity(request):
    if request.method == "POST":
        city = City()
        city.city_name = request.POST.get("city")
        city.country = request.POST.get("country_select")
        city.save()
    return HttpResponseRedirect("/")

# Delete country and cities
def delete(request, id):
    country = Country.objects.get(id=id)
    cities = City.objects.get(country=id)
    country.delete()
    cities.delete()
    return HttpResponseRedirect("/")

def update(request, id):
    country = Country.objects.get(id=id)
    cities = City.objects.all().filter(country=id)
    return render(request, "city_manager/update.html", {
        "country": country,
        "cities": cities
    })

def deleteCity(request, id):
    city = City()
    city_id = request.POST.get("city_select")
    del_city = City.objects.get(id=city_id)
    del_city.delete()
    return HttpResponseRedirect("/")

def updateCountry(request, id):
    if request.method == "POST":
        count = Country.objects.get(id=id)
        count.country_name = request.POST.get("country")
        count.save()
    return HttpResponseRedirect("/")