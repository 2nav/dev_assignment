from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm, CancelBookingForm
import django.utils

from Sports.models import Booking, Court, Inventory, Slot, Sport


def is_member(grp, user):
    return user.groups.filter(name=grp).exists()


@login_required
def home(request):
    sports = Sport.objects.all()
    return render(request, 'Sports/home.html', {'sports': sports})


@login_required
def sportsDetailView(request, id):
    sport = Sport.objects.get(id=id)
    context = {'sport': sport, 'courts': Court.objects.filter(sport=sport), 'inventories': Inventory.objects.filter(sport=sport)
               }
    return render(request, 'Sports/sport_detail.html', context)


class SlotListView(ListView):
    model = Slot
    context_object_name = 'slots'
    ordering = ['-timeStart']


@login_required
def SlotDetailView(request, id):
    if request.method == 'POST':
        slot = Slot.objects.get(id=id)
        form = BookingForm(request.POST)

        if form.is_valid():
            if len(Booking.objects.filter(booker=request.user).filter(bookingDate=django.utils.timezone.now())) > 3:
                messages.error(request, 'only 3 bookings per day')
            else:
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


@login_required
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
