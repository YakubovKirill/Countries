from django.db import models

# Country database model

class Country(models.Model):
    country_name = models.CharField(max_length=100)

# City database model

class City(models.Model):
    city_name = models.CharField(max_length=100)
    country = models.IntegerField()