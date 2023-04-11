from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='cars_index'),
    path('cars/<int:car_id>/', views.cars_detail, name='cars_details'),
    path('cars/create/', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car_delete'),
    path('drivers/', views.drivers_index, name='drivers_index'),
    path('drivers/create/', views.DriverCreate.as_view(), name='driver_create'),
    path('drivers/<int:driver_id>/', views.drivers_detail, name='drivers_detail'),
    path('drivers/<int:pk>/update/', views.DriverUpdate.as_view(), name='driver_update'),
    path('drivers/<int:pk>/delete/', views.DriverDelete.as_view(), name='driver_delete'),
    path('cars/<int:car_id>/add_service/', views.add_service, name='add_service'),
]