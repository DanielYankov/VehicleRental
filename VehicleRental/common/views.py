from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as views

from VehicleRental.common.forms import UserRateForm, VehicleReviewForm
from VehicleRental.common.models import UserRating, VehicleReview
from VehicleRental.vehicles.models import Vehicle

UserModel = get_user_model()
class Index(views.ListView):
    model = Vehicle
    template_name = 'common/home-page.html'
    ordering = ('-pk')


def update_user_rating(user_pk):
    user = UserModel.objects.filter(pk=user_pk).get()
    ratings = UserRating.objects.filter(reciever=user)
    avarage_rating = 0
    for rating in ratings:
        avarage_rating += rating.rating
    avarage_rating = round(avarage_rating / ratings.count(), 1)
    user.avarage_rating = avarage_rating
    user.save()

@login_required
def RateUser(request, pk):
    writer = request.user
    reciever = UserModel.objects.filter(pk=pk).get()
    rating_exists = UserRating.objects.filter(writer=writer, reciever=reciever).exists()
    if rating_exists:
        rating = UserRating.objects.filter(writer=writer, reciever=reciever).get()

    if request.method == 'GET' and rating_exists:
        form = UserRateForm(instance=rating)
    elif request.method == 'GET':
        form = UserRateForm()
    elif request.method == 'POST' and rating_exists:
        form = UserRateForm(request.POST, instance=rating)
        form.save()
        update_user_rating(reciever.pk)
        return redirect('details user', pk=reciever.pk)
    else:
        form = UserRateForm(request.POST)
        rating_exists = form.save(commit=False)
        rating_exists.writer = writer
        rating_exists.reciever = reciever
        form.save()
        update_user_rating(reciever.pk)
        return redirect('details user', pk=reciever.pk)

    context = {
        'form': form,
        'reciever': reciever,
    }

    return  render(request, 'accounts/user-rate-page.html', context)

@login_required
def ReviewVehicleView(request, pk):
    vehicle = Vehicle.objects.filter(pk=pk).get()
    form = VehicleReviewForm(request.POST)
    if form.is_valid():
        try:
            same_review = VehicleReview.objects.filter(vehicle=vehicle, user=request.user).get()
            same_review.delete()
        except VehicleReview.DoesNotExist:
            pass

        review = form.save(commit=False)
        review.vehicle = vehicle
        review.user = request.user
        form.save()
    return redirect('details vehicle', pk=vehicle.pk)

def DeleteReviewView(request, pk):
    review = VehicleReview.objects.filter(pk=pk).get()
    vehicle = review.vehicle
    review.delete()
    return redirect('details vehicle', pk=vehicle.pk)