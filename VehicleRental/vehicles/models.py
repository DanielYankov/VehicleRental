from django.db import models
from django.core import validators
from VehicleRental.accounts.models import AppUser
from VehicleRental.core.validators import validate_only_letters
from VehicleRental.vehicles.validators import validate_year_from_1900_to_current, validate_image_less_than_5mb


class Location(models.Model):
    MIN_LOCATION_LEN = 2
    MAX_LOCATION_LEN = 40
    name = models.CharField(
        max_length=40,
        validators=(
            validators.MinLengthValidator(MIN_LOCATION_LEN),
            validators.MaxLengthValidator(MAX_LOCATION_LEN),
            validate_only_letters,
        )
    )

    def __str__(self):
        return f'{self.name}'

class Vehicle(models.Model):
    MAX_MAKE_LEN = 30
    MAX_MODEL_LEN = 30

    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    make = models.CharField(
        max_length=MAX_MAKE_LEN,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LEN,
    )

    year = models.IntegerField(
        validators=(
            validate_year_from_1900_to_current,
        )
    )

    photo = models.ImageField(
        upload_to='car_photos',
        null = False,
        blank = False,
        validators=(
            validate_image_less_than_5mb,
        )
    )

    location = models.ForeignKey(
            Location,
            on_delete=models.CASCADE,
        )

    price_per_day = models.IntegerField(
        validators=(
            validators.MinValueValidator(0),
            validators.MaxValueValidator(1000000),
        )
    )

    def get_make_model_year(self):
        return f'{self.make} {self.model} year:{self.year}'
    def __str__(self):
        return f'({self.pk}){self.make} {self.model} {self.year}'



