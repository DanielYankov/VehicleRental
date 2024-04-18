from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from VehicleRental.common.forms import VehicleReviewForm
from VehicleRental.common.models import VehicleReview, Order
from VehicleRental.core.utils import is_owner
from VehicleRental.vehicles.forms import VehicleCreateForm, VehicleEditForm, VehicleOrderForm
from VehicleRental.vehicles.models import Vehicle


class AddVehicle(views.CreateView):
    template_name = 'vehicles/vehicle-add-page.html'
    form_class = VehicleCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DetailsVehicle(views.DetailView):
    model = Vehicle
    template_name = 'vehicles/vehicle-detail-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_vehicle = self.get_object()
        context['is_owner'] = is_owner(self.request, current_vehicle)
        context['review_form'] = VehicleReviewForm()
        context['reveiws'] = current_vehicle.vehiclereview_set.all
        context['has_reviews'] = VehicleReview.objects.filter(vehicle=current_vehicle).exists()
        return context


class EditVehicle(views.UpdateView):
    model = Vehicle
    form_class = VehicleEditForm
    template_name = 'vehicles/vehicle-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('details vehicle', kwargs={
            'pk': self.object.pk,
        })

class DeleteVehicle(views.DeleteView):
    model = Vehicle
    template_name = 'vehicles/vehicle-delete-page.html'
    success_url = reverse_lazy('index')


@login_required
def OrderVehicle(request, pk):
    user = request.user
    vehicle = Vehicle.objects.filter(pk=pk).get()
    def_order = VehicleOrderForm().save(commit=False)
    def_order.vehicle = vehicle
    if request.method == 'GET':
        form = VehicleOrderForm(instance=def_order)
    else:
        form = VehicleOrderForm(request.POST)
        if form.is_valid():

            order = form.save(commit=False)
            order.user = user
            order.vehicle = vehicle
            order.save()
            return redirect('index')

    context = {
        'form': form,
        'vehicle': vehicle,
    }

    return render(request, 'vehicles/vehicle-order-page.html', context)

def DeleteOrderView(request, pk):
    Order.objects.filter(pk=pk).delete()
    return redirect('orders user', pk=request.user.pk)








