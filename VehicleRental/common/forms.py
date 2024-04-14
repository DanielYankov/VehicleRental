from django import forms
class SearchVehicleForm(forms.Form):
    vehicle_model = forms.CharField(
        max_length=30,
        required=False,
    )