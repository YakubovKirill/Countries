from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# main page view

def index(request):
    countries = Country.objects.all()
    return render(request, "city_manager/index.html", {"countries": countries})

def addCount(request):
    if request.method == "POST":
        count = Country()
        count.country_name = request.POST.get("country")
        count.save()
    return HttpResponseRedirect("/")
