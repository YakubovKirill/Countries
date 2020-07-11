from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField

class City(models.Model):
    city_name = models.CharField
    country = models.IntegerField