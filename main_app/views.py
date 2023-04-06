from django.shortcuts import render

# dummy data

class Car:
    def __init__(self, make, model, description, year):
        self.make = make
        self.model = model
        self.description = description
        self.year = year


cars = [
    Car('Lamborghini', 'Aventador', 'Very fast car', 2020),
    Car('Rolls Royce', 'Wraith', 'Super Comfortable car', 2017),
    Car('Mercedes Benz', 'S Class', 'Very elegant car', 2018)
]

# Create your views here.

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def cars_index(request):
    return render(request, 'cars/index.html', {'cars': cars})