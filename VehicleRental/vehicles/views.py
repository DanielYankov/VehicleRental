from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from VehicleRental.core.utils import is_owner
from VehicleRental.vehicles.forms import VehicleCreateForm, VehicleEditForm, VehicleDeleteForm
from VehicleRental.vehicles.models import Vehicle

class AddVehicle(views.CreateView):
    template_name = 'vehicles/vehicle-add-page.html'
    form_class = VehicleCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Set the user of the vehicle to the current user before saving
        form.instance.user = self.request.user
        return super().form_valid(form)

class DetailsVehicle(views.DetailView):
    model = Vehicle
    template_name = 'vehicles/vehicle-detail-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_vehicle = self.get_object()
        context['is_owner'] = is_owner(self.request, current_vehicle)
        return context


class EditVehicle(views.UpdateView):
    model = Vehicle
    form_class = VehicleEditForm
    template_name = 'vehicles/vehicle-edit-page.html'  # Path to your HTML template

    def get_success_url(self):
        return reverse_lazy('details vehicle', kwargs={
            'pk': self.object.pk,
        })

class DeleteVehicle(views.DeleteView):
    model = Vehicle
    template_name = 'vehicles/vehicle-delete-page.html'  # Path to your HTML template
    success_url = reverse_lazy('index')

    # def delete(self, request, *args, **kwargs):
    #     # Get the vehicle object
    #     self.object = self.get_object()
    #     self.object.vehiclereview_set.all().delete()
    #     self.object.vehicleorder_set.all().delete()
    #     return super().delete(request, *args, **kwargs)
    
    def form_valid(self, form):
        self.object.vehiclereview_set.all().delete()
        # self.object.vehicleorder_set.all().delete()
        return super().form_valid(self)

