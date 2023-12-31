"""
URL configuration for car_insurance_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from car_insurance.views import *

urlpatterns = [

    path('clients/create_client/', create_client, name='create_client'),
    path('clients/update_client/<int:pk>/', update_client, name='update_client'),
    path('clients/get_client/<int:pk>/', get_client, name='get_client'),
    path('clients/delete_client/<int:pk>/', delete_client, name='delete_client'),
    path('clients/filter_clients/', filter_clients, name='filter_clients'),
    path('clients/', get_all_clients, name='get_all_clients'),
    path('clients/get_client_phone/', get_client_phone, name='get_client_phone'),
    path('employees/', get_all_employees, name='get_all_employees'),
    path('employees/create_employee/', create_employee, name='create_employee'),
    path('employees/update_employee/<int:pk>/', update_employee, name='update_employee'),
    path('employees/get_employee/<int:pk>/', get_employee, name='get_employee'),
    path('employees/authentification/', authentification, name='authentification'),
    path('employees/delete_employee/<int:pk>/', delete_employee, name='delete_employee'),
    path('passports/create_passport/', create_passport, name='create_passport'),
    path('passports/update_passport/<int:pk>/', update_passport, name='update_passport'),
    path('passports/get_passport/<int:pk>/', get_passport, name='get_passport'),
    path('passports/get_actual_passport/<int:client_id>', get_actual_passport, name='get_actual_passport'),
    path('passports/<int:client_id>/', get_all_passports, name='get_all_passports'),
    path('passports/get_all_passports_desc/<int:client_id>/', get_all_passports_desc, name='get_all_passports_desc'),
    path('passports/delete_passport/<int:pk>/', delete_passport, name='delete_passport'),
    path('passports/send_photo_passport/', send_photo_passport, name='send_photo_passport'),
    path('licenses/create_license/', create_license, name='create_license'),
    path('licenses/update_license/<int:pk>/', update_license, name='update_license'),
    path('licenses/get_license/<int:pk>/', get_license, name='get_license'),
    path('licenses/get_actual_license/<int:client_id>', get_actual_license, name='get_actual_license'),
    path('licenses/<int:client_id>/', get_all_licenses, name='get_all_licenses'),
    path('licenses/get_all_licenses_desc/<int:client_id>/', get_all_licenses_desc, name='get_all_licenses_desc'),
    path('licenses/delete_license/<int:pk>/', delete_license, name='delete_license'),
    path('cars/create_car/', create_car, name='create_car'),
    path('cars/update_car/<int:pk>/', update_car, name='update_car'),
    path('cars/get_car/<int:pk>/', get_car, name='get_car'),
    path('cars/<int:client_id>/', get_all_cars, name='get_all_cars'),
    path('cars/delete_car/<int:pk>/', delete_car, name='delete_car'),
    path('cars/filter_cars/', filter_cars, name='filter_cars'),
    


]
