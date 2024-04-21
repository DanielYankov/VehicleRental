from enum import Enum
from django.db import models
from django.contrib.auth import models as auth_models
from django.core import validators
from VehicleRental.core.validators import validate_only_letters, validate_all_capital


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())

class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'

class Currency(models.Model):
    MAX_CURRENCY_LEN = 3

    name = models.CharField(
        max_length=MAX_CURRENCY_LEN,
        validators=(
            validate_all_capital,
        ),
        null=False,
        blank=False,
        unique=True,
    )

    price_to_bgn = models.FloatField(
        validators=(
            validators.MinValueValidator(0.0),
        ),
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAN_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAN_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAN_LEN_FIRST_NAME,
        validators = (
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=MAN_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        ),
        blank=True,
        null=True,
    )
    email = models.EmailField(
        unique=True,
    )
    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
        blank=True,
        null=True,
    )

    avarage_rating = models.FloatField(
        default=0,
        null=True,
        blank=True
    )

    currency = models.ForeignKey(
        Currency,
        on_delete=models.RESTRICT,
        default=1,
    )




