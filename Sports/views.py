from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm, CancelBookingForm

from Sports.models import Booking, Court, Inventory, Slot, Sport


@login_required
def home(request):
    sports = Sport.objects.all()
    return render(request, 'Sports/home.html', {'sports': sports})


def sportsDetailView(request, id):
    sport = Sport.objects.get(id=id)
    context = {'sport': sport, 'courts': Court.objects.filter(sport=sport), 'inventories': Inventory.objects.filter(sport=sport)
               }
    return render(request, 'Sports/sport_detail.html', context)


class SlotListView(ListView):
    model = Slot
    context_object_name = 'slots'
    ordering = ['-timeStart']


def SlotDetailView(request, id):
    if request.method == 'POST':
        slot = Slot.objects.get(id=id)
        form = BookingForm(request.POST)

        if form.is_valid():

            form.instance.booker = request.user
            form.instance.status = True
            # form.save()
            slot.available = False
            slot.save()
            form.instance.slot = Slot.objects.get(id=id)
            form.save()
            messages.success(
                request, f'Request for slot successfully approved')
    else:
        form = BookingForm()
        slot = Slot.objects.get(id=id)
    return render(request, 'Sports/slot_detail.html', {'object': slot, 'form': form})


class BookingListView(ListView):
    model = Booking
    context_object_name = 'bookings'
    ordering = ['-bookingTime']


def BookingDetailView(request, id):
    if request.method == 'POST':
        booking = Booking.objects.get(id=id)
        form = CancelBookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.instance.slot.available = True
            form.instance.booker = request.user
            # form.save()

            form.instance.slot.save()
            form.instance.status = False
            form.save()
            messages.success(
                request, f'Booking successfully cancelled')
    else:
        booking = Booking.objects.get(id=id)
        form = CancelBookingForm(instance=booking)
    return render(request, 'Sports/booking_detail.html', {'object': booking, 'form': form})
