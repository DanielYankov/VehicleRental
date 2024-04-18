from django import forms

from VehicleRental.common.models import VehicleReview, UserRating


class SearchVehicleForm(forms.Form):
    vehicle_model = forms.CharField(
        max_length=30,
        required=False,
    )

class VehicleReviewForm(forms.ModelForm):
    class Meta:
        model = VehicleReview
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add review...',
                }
            )
        }

class UserRateForm(forms.ModelForm):
    class Meta:
        model = UserRating
        fields = ('rating',)