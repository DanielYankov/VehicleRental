from django.contrib import admin

from VehicleRental.vehicles.models import Vehicle, Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    # list_display = ('pk', 'make', 'model', 'year')
    pass
    