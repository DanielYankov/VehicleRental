from django import forms
from django.core.exceptions import ValidationError

from VehicleRental.common.models import Order
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

class VehicleOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('vehicle', 'date_from', 'date_to', )
        widgets = {
            'date_from': forms.SelectDateWidget(),
            'date_to': forms.SelectDateWidget(),
            'vehicle': forms.HiddenInput(),
        }

    def clean_date_to(self):
        date_to = self.cleaned_data['date_to']
        date_from = self.cleaned_data['date_from']
        current_vehicle = self.cleaned_data['vehicle']
        if date_to < date_from:
            raise ValidationError('"Date to" date cannot be before "Date from" date ')
        for order in Order.objects.filter(vehicle=current_vehicle):
            if (order.date_from <= date_from and order.date_to >= date_from) or (order.date_from <= date_to and order.date_to >= date_to):
                raise ValidationError('The vehicle is not available at those days')

        return date_to

