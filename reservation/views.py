from django.shortcuts import render, redirect, get_object_or_404
from main.models import HotelRoom
from .models import Reservation
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime, date
from django.db import transaction

# Create your views here.

def reservation_page(request, pk):
    selected_room = get_object_or_404(HotelRoom, id=pk)
    info = {'room':selected_room}
    return render(request, 'reservation_page.html', info)

def reservation_checkout(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, You must be signed in to an account first.')
        return redirect('home_page')

    if request.method != 'POST':
        messages.error(request, 'Sorry, This request is not allowed.')
        return redirect('home_page')

    user = request.user
    room_id = request.POST.get('room_id')
    arrival = request.POST.get('arrival')
    departure = request.POST.get('departure')

    if not room_id:
        messages.error(request, 'Sorry, The selected room is invalid.')
        return redirect('home_page')

    if not arrival or not departure:
        messages.error(request, 'Sorry, Arrival and departure dates cannot be empty.')
        return redirect('reservation_page', pk=room_id)

    try:
        arrival_date = datetime.strptime(arrival, '%Y-%m-%d').date()
        departure_date = datetime.strptime(departure, '%Y-%m-%d').date()
    except ValueError:
        messages.error(request, 'Sorry, You have entered invalid dates.')
        return redirect('reservation_page', pk=room_id)

    if arrival_date >= departure_date:
        messages.error(request, 'Sorry, You have entered invalid dates.')
        return redirect('reservation_page', pk=room_id)

    if arrival_date < date.today():
        messages.error(request, 'Sorry, Arrival date cannot be in the past.')
        return redirect('reservation_page', pk=room_id)

    nights = (departure_date - arrival_date).days

    if nights > 30:
        messages.error(request,'Sorry, The maximum reservation period is 30 nights.')
        return redirect('reservation_page', pk=room_id)

    with transaction.atomic():
        selected_room = get_object_or_404(
            HotelRoom.objects.select_for_update(),
            id=room_id
        )

        if not selected_room.is_in_service:
            messages.error(request, 'Sorry, This room is currently out of service.')
            return redirect('reservation_page', pk=room_id)

        conflict = Reservation.objects.filter(
            room=selected_room,
            arrival_date__lt=departure_date,
            departure_date__gt=arrival_date,
        ).exists()

        if conflict:
            messages.error('Sorry, This room is already booked for the selected dates.')
            return redirect('reservation_page', pk=room_id)

        if selected_room.is_sale:
            total_price = (selected_room.sale_price_per_night * nights)
        else:
            total_price = (selected_room.price_per_night * nights)

        Reservation.objects.create(
            user=user,
            room=selected_room,
            arrival_date=arrival_date,
            departure_date=departure_date,
            total_price=total_price,
        )

    messages.success(request,'Your reservation has been registered.')

    return redirect('home_page')
    
def reservation_cancel(request, pk):
    selcted_reservation = get_object_or_404(Reservation, id=pk)
    selcted_reservation.status = 'cancelled'
    selcted_reservation.save()
    messages.success(request, ('Your reservation has been cancelled.'))
    return redirect('profile_page')
