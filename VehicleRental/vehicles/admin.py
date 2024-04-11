from django.contrib import admin

from VehicleRental.vehicles.models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    # list_display = ('pk', 'make', 'model', 'year')
    pass
    