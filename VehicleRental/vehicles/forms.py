from django import forms

from VehicleRental.common.models import VehicleReview, Order
from VehicleRental.vehicles.models import Vehicle

class BaseVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('user',)

class VehicleCreateForm(BaseVehicleForm):
    pass


class VehicleEditForm(BaseVehicleForm):
    pass

class VehicleDeleteForm(BaseVehicleForm):

    def save(self, commit=True):
        vehicle = super().save(commit=False)
        vehicle.vehiclereview_set.all().delete()
        vehicle.vehicleorder_set.all().delete()
        vehicle.delete()
        return vehicle