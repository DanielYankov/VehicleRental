from django.urls import path

from VehicleRental.accounts.views import LogInView, SignUpView, LogOutView

urlpatterns = (
    path('login/', LogInView.as_view(), name ='login user'),
    path('register/', SignUpView.as_view(), name = 'signup user'),
    path('logout/', LogOutView.as_view(), name ='logout user'),
)