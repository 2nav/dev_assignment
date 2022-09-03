from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm

from Sports.models import Court, Inventory, Slot, Sport


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
            form.instance.slot = Slot.objects.get(id=id)
            # form.save()
            slot.available = False
            slot.save()
            form.instance.status = True
            form.save()
            messages.success(
                request, f'Request for slot successfully approved')
    else:
        form = BookingForm()
        slot = Slot.objects.get(id=id)
    return render(request, 'Sports/slot_detail.html', {'object': slot, 'form': form})
