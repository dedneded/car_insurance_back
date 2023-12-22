from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.test import TestCase
from .serializers import *
from rest_framework.test import APIClient
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes


@api_view(['POST'])
def create_client(request):
    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_client_phone(request):
    phone = request.GET.get('phone', None)
    client = None
    if phone:
        client = Client.objects.filter(Phone__icontains=phone)
    # Используем сериализатор для преобразования результатов в JSON
    serializer = ClientSerializer(client, many=True)
    
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # РџСЂРѕРІРµСЂСЏРµРј, СЃРІСЏР·Р°РЅ Р»Рё РєР»РёРµРЅС‚ СЃ РЅРµСѓРґР°Р»РµРЅРЅС‹Рј РїР°СЃРїРѕСЂС‚РѕРј
    if Passport.objects.filter(Client=client, DateDel__isnull=True).exists():
        return Response({"message": "Cannot delete employee. It is associated with active clients."},
                        status=status.HTTP_409_CONFLICT)
    client.DateDel = datetime.now()
    client.save()

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_all_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def filter_clients(request):
    phone = request.GET.get('phone', None)
    email = request.GET.get('email', None)
    clients = None
    if phone and email:
        clients = Client.objects.filter(Phone__icontains=phone, Email__icontains=email)
    elif phone:
        clients = Client.objects.filter(Phone__icontains=phone)
    elif email:
        clients = Client.objects.filter(Email__icontains=email)
    
    # Используем сериализатор для преобразования результатов в JSON
    serializer = ClientSerializer(clients, many=True)
    
    return Response(serializer.data)


@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_employee(request, pk):
    try:
        print(pk)
        employee = Employee.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def authentification(request):
    try:
        phone = request.data.get('phone')
        password = request.data.get('password')
        employee = Employee.objects.get(Phone=phone, Password=password)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # РџСЂРѕРІРµСЂСЏРµРј, СЃРІСЏР·Р°РЅ Р»Рё СЃРѕС‚СЂСѓРґРЅРёРє СЃ РЅРµСѓРґР°Р»РµРЅРЅС‹Рј РєР»РёРµРЅС‚РѕРј
    if Client.objects.filter(Employee=employee, DateDel__isnull=True).exists():
        return Response({"message": "Cannot delete employee. It is associated with active clients."},
                        status=status.HTTP_409_CONFLICT)
    employee.DateDel = datetime.now()
    employee.save()

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_all_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_passport(request):
    serializer = PassportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def send_photo_passport(request):
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_passport(request, pk):
    try:
        passport = Passport.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PassportSerializer(passport, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_passport(request, pk):
    try:
        passport = Passport.objects.get(pk=pk)
        serializer = PassportSerializer(passport)
        return Response(serializer.data)

    except ObjectDoesNotExist as e:
        print(str(e))
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_actual_passport(request, client_id):
    try:
        passport = Passport.objects.filter(Client=client_id).order_by('-DateOfIssue')
        if passport:
                passport = passport[0]
        else:
                passport = None
        serializer = PassportSerializer(passport)
        return Response(serializer.data)

    except ObjectDoesNotExist as e:
        print(str(e))
        return Response(status=status.HTTP_404_NOT_FOUND)
	

@api_view(['GET'])
def get_all_passports(request, client_id):
    try:
        passports = Passport.objects.filter(Client=client_id).order_by('DateOfIssue')
        serializer = PassportSerializer(passports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Passport.DoesNotExist:
        return Response("Passports not found for the specified client.", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_passports_desc(request, client_id):
    try:
        passports = Passport.objects.filter(Client=client_id).order_by('-DateOfIssue')
        serializer = PassportSerializer(passports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Passport.DoesNotExist:
        return Response("Passports not found for the specified client.", status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_passport(request, pk):
    try:
        passport = Passport.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    passport.DateDel = datetime.now()
    passport.save()

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_license(request):
    serializer = LicenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_license(request, pk):
    try:
        license = License.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = LicenseSerializer(license, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_license(request, pk):
    try:
        license = License.objects.get(pk=pk)
        serializer = LicenseSerializer(license)
        return Response(serializer.data)

    except ObjectDoesNotExist as e:
        print(str(e))
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_actual_license(request, client_id):
    try:
        license = License.objects.filter(Client=client_id).order_by('-DateOfIssue')
        if license:
                license= license[0]
        else:
                license = None
        serializer = LicenseSerializer(license)
        return Response(serializer.data)

    except ObjectDoesNotExist as e:
        print(str(e))
        return Response(status=status.HTTP_404_NOT_FOUND)
	

@api_view(['GET'])
def get_all_licenses(request, client_id):
    try:
        licenses = License.objects.filter(Client=client_id).order_by('DateOfIssue')
        serializer = LicenseSerializer(licenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except License.DoesNotExist:
        return Response("Licenses not found for the specified client.", status=status.HTTP_404_NOT_FOUND)

   
@api_view(['GET'])
def get_all_licenses_desc(request, client_id):
    try:
        licenses = License.objects.filter(Client=client_id).order_by('-DateOfIssue')
        serializer = LicenseSerializer(licenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except License.DoesNotExist:
        return Response("Licenses not found for the specified client.", status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_license(request, pk):
    try:
        license = License.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    license.DateDel = datetime.now()
    license.save()

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_car(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CarSerializer(car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_car(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    except ObjectDoesNotExist as e:
        print(str(e))
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_cars(request, client_id):
    try:
        cars = Car.objects.filter(Client=client_id)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Car.DoesNotExist:
        return Response("Cars not found for the specified client.", status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_car(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    car.DateDel = datetime.now()
    car.save()

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def filter_cars(request):
    registration_num = request.GET.get('registrationNumber', None)
    cars = None
    if registration_num:
        cars = Car.objects.filter(RegistrationNumber__icontains=registration_num)
    # Используем сериализатор для преобразования результатов в JSON
    serializer = CarSerializer(cars, many=True)
    
    return Response(serializer.data)



