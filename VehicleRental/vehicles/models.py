from django.db import models

from VehicleRental.vehicles.validators import validate_year_from_1900_to_current, validate_image_less_than_5mb


class Vehicle(models.Model):
    MAX_MAKE_LEN = 30
    MAX_MODEL_LEN = 30


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
        blank = True,
        validators=(
            validate_image_less_than_5mb,
        )
    )

    def __str__(self):
        return f'({self.pk}){self.make} {self.model} {self.year}'



