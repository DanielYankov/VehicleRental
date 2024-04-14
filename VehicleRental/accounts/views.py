from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

# from Petstagram.accounts.forms import UserCreateForm

# Create your views here.
UserModel = get_user_model()
class LogInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    # success_url = reverse_lazy('index')

class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    # form_class = UserCreateForm
    success_url = reverse_lazy('index')

class LogOutView(auth_views.LogoutView):
    pass
