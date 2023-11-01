from django.db import models
from django.db.models import Model


class Country(Model):
    name = models.CharField(max_length=50)


class City(Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class Flight(Model):
    arrival_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="arr_city"
    )
    departure_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="dep_city"
    )
    arrival_date = models.DateTimeField("date arrived")
    departure_date = models.DateTimeField("date departured")


class Hotel(Model):
    class Stars(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stars = models.IntegerField(choices=Stars.choices)
    price_per_night = models.DecimalField(max_digits=9, decimal_places=2)
    accomodation_type = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    food_type = models.CharField(max_length=30)


class Tour(Model):
    arrival_flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name="arr_flight"
    )
    departure_flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name="dep_flight"
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    visa_available = models.BooleanField()


class Client(Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    passport = models.CharField(max_length=30)
    foreign_passport = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    visa_date = models.CharField(max_length=30)


class Sale(Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(max_length=50)
