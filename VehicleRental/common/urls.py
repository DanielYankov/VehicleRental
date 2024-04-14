from django.urls import path
from VehicleRental.common.views import Index

urlpatterns = (
    path('', Index.as_view(), name='index'),
)