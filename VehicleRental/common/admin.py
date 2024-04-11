from django.contrib import admin

from VehicleRental.common.models import Location, Listing, Order, UserRating, VehicleReview


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):
    pass

@admin.register(VehicleReview)
class VehicleReviewAdmin(admin.ModelAdmin):
    pass