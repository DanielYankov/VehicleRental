from django.shortcuts import render
from django.views import generic as views

from VehicleRental.common.forms import SearchVehicleForm
from VehicleRental.vehicles.models import Vehicle


class Index(views.ListView):
    model = Vehicle
    template_name = 'common/home-page.html'