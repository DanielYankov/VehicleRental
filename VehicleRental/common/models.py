from enum import Enum

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

    RATING_CHOICES = [
        (1, 'Horrible'),
        (2, 'Bad'),
        (3, 'Avarage'),
        (4, 'Good'),
        (5, 'Excellent'),
    ]

    rating = models.IntegerField(
        choices=RATING_CHOICES,
    )

    writer = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='writer_set',
    )

    reciever = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
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
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user} about: {self.vehicle}'

class Order(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,

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



