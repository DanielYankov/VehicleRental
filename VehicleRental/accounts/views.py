from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from VehicleRental.accounts.forms import UserCreateForm
from VehicleRental.common.models import UserRating, Order


# Create your views here.
UserModel = get_user_model()
class LogInView(auth_views.LoginView):
    template_name = 'accounts/user-login-page.html'

class SignUpView(views.CreateView):
    template_name = 'accounts/user-register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

class LogOutView(auth_views.LogoutView):
    pass

class UserEditView(views.UpdateView):
    model = UserModel
    template_name = 'accounts/user-edit-page.html'
    fields = ('first_name', 'last_name', 'gender', 'currency')
    def get_success_url(self):
        return  reverse_lazy('details user', kwargs ={
            'pk': self.request.user.pk,
        })

class UserDeleteView(views.DeleteView):
    template_name = 'accounts/user-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

class UserDetailsView(views.DetailView):
    template_name = 'accounts/user-details-page.html'
    model = UserModel


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.get_object()
        vehicles = current_user.vehicle_set.all()
        rating_stars = round(current_user.avarage_rating)
        ratings_count = UserRating.objects.filter(reciever=current_user).count()
        context['vehicles'] = vehicles
        context['vehicle_count'] = vehicles.count()
        context['is_owner'] = self.request.user == self.object
        context['full_stars_count'] = range(rating_stars)
        context['empty_stars_count'] = range(5 - rating_stars)
        context['ratings_count'] = ratings_count
        return context

def UserOrdersView(request, pk):
    if request.user != UserModel.objects.filter(pk=pk).get():
        return redirect('index')
    orders = Order.objects.filter(user_id=pk).all()
    context = {
        'orders': orders,
        'user': UserModel.objects.filter(pk=pk).get()
    }
    return render(request, 'accounts/user-orders-page.html', context)
