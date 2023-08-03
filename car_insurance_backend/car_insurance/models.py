from django.db import models
from datetime import datetime
from datetime import date


class Client(models.Model):
    Phone = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    DateAdd = models.DateTimeField(null=False, blank=False, default=datetime.now())
    DateDel = models.DateTimeField(null=True, blank=True)
    Employee = models.ForeignKey('Employee', on_delete=models.PROTECT, null=True, blank=True)
    objects = models.Manager()


class Employee(models.Model):
    FIO = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    IsAdmin = models.BooleanField(default=False)
    DateOfBirth = models.DateTimeField(null=False, blank=False)
    DateAdd = models.DateTimeField(null=False, blank=False, default=datetime.now())
    DateDel = models.DateTimeField(null=True, blank=True)
    objects = models.Manager()

    def __repr__(self):
        return f"Employee(FIO='{self.FIO}', Phone='{self.Phone}', Email='{self.Email}',Password='{self.Password}'," \
               f", DateAdd='{self.DateAdd}',DateOfBirth='{self.DateOfBirth}',DateDel ='{self.DateDel}')"


class Passport(models.Model):
    IssuedByWhom = models.CharField(max_length=500)
    DateOfIssue = models.DateTimeField(null=False, blank=False)
    DivisionCode = models.CharField(max_length=255)
    Series = models.CharField(max_length=255)
    Number = models.CharField(max_length=255)
    FIO = models.CharField(max_length=255)
    IsMale = models.BooleanField(default=True)
    DateOfBirth = models.DateTimeField(null=False, blank=False, default=date.today())
    PlaceOfBirth = models.CharField(max_length=500)
    ResidenceAddress = models.CharField(max_length=500)
    DateDel = models.DateTimeField(null=True, blank=True)
    Client = models.ForeignKey('Client', on_delete=models.PROTECT)
    Photos = models.ManyToManyField('PassportPhoto', null=True, blank=True)
    objects = models.Manager()


class License(models.Model):
    DateOfIssue = models.DateTimeField(null=False, blank=False)
    ExpirationDate = models.DateTimeField(null=False, blank=False)
    CodeGIBDD = models.CharField(max_length=255)
    Series = models.CharField(max_length=255)
    Number = models.CharField(max_length=255)
    TransmissionType = models.CharField(max_length=255)
    VehicleCategories = models.CharField(max_length=255)
    DateDel = models.DateTimeField(null=True, blank=True)
    Client = models.ForeignKey('Client', on_delete=models.PROTECT)
    Photos = models.ManyToManyField('LicensePhoto', null=True, blank=True)
    objects = models.Manager()


class Car(models.Model):
    RegistrationNumber = models.CharField(max_length=255)
    IdNumber = models.CharField(max_length=255)
    Brand = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    TCType = models.CharField(max_length=255)
    TCCategory = models.CharField(max_length=255)
    YearOfIssue = models.IntegerField(null=False, blank=False)
    EngineModel = models.CharField(max_length=255)
    EngineNumber = models.CharField(max_length=255)
    ChassisNumber = models.CharField(max_length=255)
    CarBodyNumber = models.CharField(max_length=255)
    Color = models.CharField(max_length=255)
    EnginePower = models.CharField(max_length=255)
    EngineDisplacement = models.IntegerField(null=False, blank=False)
    Series = models.CharField(max_length=255)
    Number = models.CharField(max_length=255)
    MaxWeightPermitted = models.IntegerField(null=False, blank=False)
    WeightWithoutCapacity = models.IntegerField(null=False, blank=False)
    NameOwner = models.CharField(max_length=255)
    PlaceRegistration = models.CharField(max_length=255)
    PlaceOfIssue = models.CharField(max_length=255)
    DateOfIssue = models.DateTimeField(null=False, blank=False)
    DateDel = models.DateTimeField(null=True, blank=True)
    Client = models.ForeignKey('Client', on_delete=models.PROTECT)
    Photos = models.ManyToManyField('CarPhoto', null=True, blank=True)
    objects = models.Manager()


class PassportPhoto(models.Model):
    DateDel = models.DateTimeField(null=True, blank=True)
    Path = models.ImageField(upload_to="photos/")


class LicensePhoto(models.Model):
    DateDel = models.DateTimeField(null=True, blank=True)
    Path = models.ImageField(upload_to="photos/")


class CarPhoto(models.Model):
    DateDel = models.DateTimeField(null=True, blank=True)
    Path = models.ImageField(upload_to="photos/")
