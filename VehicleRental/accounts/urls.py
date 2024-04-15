from django.urls import path, include

from VehicleRental.accounts.views import LogInView, SignUpView, LogOutView, UserEditView, UserDetailsView, \
    UserDeleteView

urlpatterns = (
    path('login/', LogInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='signup user'),
    path('logout/', LogOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ]))
)
