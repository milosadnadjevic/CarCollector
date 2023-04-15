from django.shortcuts import render, redirect
from .models import Car
from .models import Driver
from .forms import ServiceForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

@login_required
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

@login_required
def assoc_driver(request, car_id, driver_id):
    car = Car.objects.get(id=car_id)
    car.drivers.add(driver_id)
    return redirect('cars_details', car_id=car_id)

@login_required
def unassoc_driver(request, car_id, driver_id):
    car = Car.objects.get(id=car_id)
    car.drivers.remove(driver_id)
    return redirect('cars_details', car_id=car_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
         user = form.save()
         login(request, user)
         return redirect('cars_index')
        else:
            error_message = 'Invalid signup - try again'

    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form , 'error': error_message})


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ('make', 'model', 'description', 'year')
    template_name = 'cars/car_form.html'
    # success_url = '/cars/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarUpdate(LoginRequiredMixin,UpdateView):
    model = Car
    fields = ('description', 'year')
    template_name = 'cars/car_form.html'

class CarDelete(LoginRequiredMixin,DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'cars/car_confirm_delete.html'

def drivers_index(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/index.html', {'drivers': drivers})

class DriverCreate(LoginRequiredMixin,CreateView):
     model = Driver
     fields = '__all__'
     template_name = 'drivers/drivers_form.html'
     success_url = '/drivers/'

def drivers_detail(request, driver_id):
     driver = Driver.objects.get(id=driver_id)
     return render(request, 'drivers/detail.html', {'driver': driver })

class DriverUpdate(LoginRequiredMixin,UpdateView):
     model = Driver
     fields = ('__all__') 
     template_name = 'drivers/drivers_form.html'
     success_url = '/drivers/'

class DriverDelete(LoginRequiredMixin,DeleteView):
     model = Driver
     success_url = '/drivers/'
     template_name = 'drivers/driver_confirm_delete.html'