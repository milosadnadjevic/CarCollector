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
    

class Driver(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField(default=10)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('drivers_detail', kwargs={'pk': self.id})
    

class Service(models.Model):
    CAR_PART = (
        ('T', 'Tires'),
        ('E', 'Engine'),
        ('I', 'Interior')
    )
    date = models.DateField('service_date')
    car_part = models.CharField(max_length=1, choices=CAR_PART, default=CAR_PART[0][0])
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_car_part_display()} on {self.date}'