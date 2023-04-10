from django.db import models
from django.urls import reverse

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField(default=2020)

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('cars_details', kwargs={'car_id': self.id})