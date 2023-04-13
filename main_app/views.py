from django.shortcuts import render, redirect
from .models import Car
from .models import Driver
from .forms import ServiceForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# dummy data

# class Car:
#     def __init__(self, make, model, description, year):
#         self.make = make
#         self.model = model
#         self.description = description
#         self.year = year


# cars = [
#     Car('Lamborghini', 'Aventador', 'Very fast car', 2020),
#     Car('Rolls Royce', 'Wraith', 'Super Comfortable car', 2017),
#     Car('Mercedes Benz', 'S Class', 'Very elegant car', 2018)
# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    service_form = ServiceForm()
    car_driver_ids = car.drivers.all().values_list('id')
    car_driver_cantdrive = Driver.objects.exclude(id__in=car_driver_ids)
    return render(request, 'cars/detail.html', {'car': car, 'service_form': service_form, 'drivers': car_driver_cantdrive})

def add_service(request, car_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.car_id = car_id
        new_service.save()
    return redirect('cars_details', car_id=car_id)

def assoc_driver(request, car_id, driver_id):
    car = Car.objects.get(id=car_id)
    car.drivers.add(driver_id)
    return redirect('cars_details', car_id=car_id)

def unassoc_driver(request, car_id, driver_id):
    car = Car.objects.get(id=car_id)
    car.drivers.remove(driver_id)
    return redirect('cars_details', car_id=car_id)

class CarCreate(CreateView):
    model = Car
    fields = ('__all__' )
    template_name = 'cars/car_form.html'
    # success_url = '/cars/'


class CarUpdate(UpdateView):
    model = Car
    fields = ('description', 'year')
    template_name = 'cars/car_form.html'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'cars/car_confirm_delete.html'

def drivers_index(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/index.html', {'drivers': drivers})

class DriverCreate(CreateView):
     model = Driver
     fields = '__all__'
     template_name = 'drivers/drivers_form.html'
     success_url = '/drivers/'

def drivers_detail(request, driver_id):
     driver = Driver.objects.get(id=driver_id)
     return render(request, 'drivers/detail.html', {'driver': driver })

class DriverUpdate(UpdateView):
     model = Driver
     fields = ('__all__') 
     template_name = 'drivers/drivers_form.html'
     success_url = '/drivers/'

class DriverDelete(DeleteView):
     model = Driver
     success_url = '/drivers/'
     template_name = 'drivers/driver_confirm_delete.html'