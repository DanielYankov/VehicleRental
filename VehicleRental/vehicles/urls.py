from django.contrib.auth.decorators import login_required
from django.urls import path, include, reverse_lazy

from VehicleRental.vehicles.views import AddVehicle, DetailsVehicle, EditVehicle, DeleteVehicle

urlpatterns = (
    path('add/', login_required(AddVehicle.as_view(), login_url=reverse_lazy('login user')), name='add vehicle'),
    path('<int:pk>/', include([
        path('', DetailsVehicle.as_view(), name='details vehicle'),
        path('edit/', EditVehicle.as_view(), name='edit vehicle'),
        path('delete/', DeleteVehicle.as_view(), name='delete vehicle')
    ]))
)

