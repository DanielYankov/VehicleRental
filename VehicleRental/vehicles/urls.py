from django.contrib.auth.decorators import login_required
from django.urls import path, include, reverse_lazy

from VehicleRental.common.views import ReviewVehicleView, DeleteReviewView
from VehicleRental.vehicles.views import AddVehicle, DetailsVehicle, EditVehicle, DeleteVehicle, OrderVehicle, \
    DeleteOrderView

urlpatterns = (
    path('add/', login_required(AddVehicle.as_view(), login_url=reverse_lazy('login user')), name='add vehicle'),
    path('<int:pk>/', include([
        path('', DetailsVehicle.as_view(), name='details vehicle'),
        path('edit/', EditVehicle.as_view(), name='edit vehicle'),
        path('delete/', DeleteVehicle.as_view(), name='delete vehicle'),
        path('order/', OrderVehicle, name='order vehicle'),
        path('review/', ReviewVehicleView, name='reveiw vehicle'),
    ])),
    path('order/<int:pk>/', DeleteOrderView, name='delete order'),
    path('reveiw/<int:pk>/', DeleteReviewView, name='delete review'),
)

