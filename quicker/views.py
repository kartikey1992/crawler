from django.shortcuts import render
from .models import *

# Create your views here.
def get_company_location(company):
    company = company.split("<span>")
    location = company[1].split("</span>")[0].replace(' ','')
    company = company[0].replace(' ','')[6:]
    return company,location


def save_data(car_link,car_description,car_company,car_price,car_location):
    company, _created = Car_Company.objects.get_or_create(name=car_company)
    check_already_car_present = Car.objects.filter(url=car_link).exists()
    if not check_already_car_present:
        car = Car(url=car_link,company=company,price=car_price,model_description=car_description,location=car_location)
        car.save()
