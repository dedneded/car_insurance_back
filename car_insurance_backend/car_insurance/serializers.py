from rest_framework import serializers
from .models import *
from django.core.exceptions import ObjectDoesNotExist


class EmployeeSerializer(serializers.ModelSerializer):
    DateDel = serializers.DateTimeField(allow_null=True, required=False)

    class Meta:
        model = Employee

        fields = ['id','FIO', 'Phone', 'Email', 'Password', 'DateOfBirth', 'DateAdd', 'DateDel']


class ClientSerializer(serializers.ModelSerializer):
    Employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    class Meta:
        model = Client
        fields = ['id','Phone', 'Email', 'DateAdd', 'DateDel', 'Employee']


class PassportPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassportPhoto
        fields = '__all__'


class PassportSerializer(serializers.ModelSerializer):
    Photos = PassportPhotoSerializer(many=True, required=False)
    Client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Passport
        fields = '__all__'

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', None)
        passport = Passport.objects.create(**validated_data)

        if photos_data:
            for photo_data in photos_data:
                PassportPhoto.objects.create(passport=passport, **photo_data)

        return passport

class LicensePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = LicensePhoto
        fields = '__all__'


class LicenseSerializer(serializers.ModelSerializer):
    Photos = PassportPhotoSerializer(many=True, required=False)
    Client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
            model = License
            fields = '__all__'

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', None)
        license = License.objects.create(**validated_data)

        if photos_data:
            for photo_data in photos_data:
                LicensePhoto.objects.create(license=license, **photo_data)

        return license


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    Photos = PassportPhotoSerializer(many=True, required=False)
    Client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', None)
        car = Car.objects.create(**validated_data)

        if photos_data:
            for photo_data in photos_data:
                CarPhoto.objects.create(car=car, **photo_data)

        return car

