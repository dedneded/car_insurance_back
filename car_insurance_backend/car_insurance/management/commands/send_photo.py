from django.core.management.base import BaseCommand
from django.http import HttpRequest
from django.test import RequestFactory
from car_insurance.views import *

class Command(BaseCommand):
    help = 'Your custom command description'

    def handle(self, *args, **options):
        # Создаем фабрику запросов
        factory = RequestFactory()

        # Создаем POST-запрос с файлом (замените путь к файлу на свой)
        request = factory.post('http://127.0.0.1:8000/passports/send_photo_passport/', {'key': 'value'}, {'passport_photo': open('/home/car_insurance/car_insurance_backend/car_insurance_backend/car_insurance/management/commands/wbXQLqBsfGj4GDF0kJEP1HQnpSc-19201.jpg', 'rb')})

        # Вызываем метод
        response = send_photo_passport(request)

        # Печатаем результат
        self.stdout.write(self.style.SUCCESS(f"Response: {response.content}"))