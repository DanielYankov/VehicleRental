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
    class Meta:
        model = Vehicle
        exclude = ('user', 'photo')
        # TODO add photo change

class VehicleDeleteForm(BaseVehicleForm):

    def save(self, commit=True):
        vehicle = super().save(commit=False)
        vehicle.vehiclereview_set.all().delete()
        vehicle.vehicleorder_set.all().delete()
        vehicle.delete()
        return vehicle