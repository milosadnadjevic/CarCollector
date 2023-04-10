from django.shortcuts import render
from .models import Car
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
    return render(request, 'cars/detail.html', {'car': car})



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