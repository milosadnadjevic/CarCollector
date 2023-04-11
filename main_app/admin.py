from django.contrib import admin

# Register your models here.
from .models import Car, Service

admin.site.register(Car)
admin.site.register(Service)