from django.contrib import admin

from VehicleRental.accounts.models import Currency
from VehicleRental.common.models import Order, UserRating, VehicleReview

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('user',)

@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):
    ordering = ('reciever',)

@admin.register(VehicleReview)
class VehicleReviewAdmin(admin.ModelAdmin):
    ordering = ('vehicle',)

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    ordering = ('name',)