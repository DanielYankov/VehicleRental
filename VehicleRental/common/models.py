from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.core import validators
from VehicleRental.core.validators import validate_only_letters
from VehicleRental.vehicles.models import Vehicle

UserModel = get_user_model()
class UserRating(models.Model):
    MAX_RATING = 5
    MIN_RATING = 1

    rating = models.IntegerField(
        validators=(
            MaxValueValidator(MAX_RATING),
            MinValueValidator(MIN_RATING),
        )
    )

    writer = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        related_name='writer_set',
    )

    reciever = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        related_name='reciever_set',
    )

    def __str__(self):
        return f"From: {self.writer} To: {self.reciever} {self.rating * '*'}"

class VehicleReview(models.Model):
    MAX_TEXT_LEN = 300

    text = models.CharField(
        max_length=MAX_TEXT_LEN,
        blank=False,
        null=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.RESTRICT,
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return f'{self.user} about: {self.vehicle}'

class Order(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.RESTRICT,
    )

    date_from = models.DateField(
        blank=False,
        null=False,
    )
    # TODO add validation
    date_to = models.DateField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'"{self.user}" orders "{self.vehicle}" from: {self.date_from} to : {self.date_to}'

class Location(models.Model):
    MIN_LOCATION_LEN = 2
    MAX_LOCATION_LEN = 40
    name = models.CharField(
        max_length=40,
        validators=(
            validators.MinLengthValidator(MIN_LOCATION_LEN),
            validate_only_letters,
        )
    )

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):
    vehicle =models.OneToOneField(
        Vehicle,
        on_delete=models.RESTRICT,
    )

    price_per_day = models.IntegerField(
        validators=(
            validators.MinValueValidator(0),
        )
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return f'{self.vehicle} for {self.price_per_day}BGN in {self.location}'


