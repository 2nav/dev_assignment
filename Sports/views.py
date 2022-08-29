from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Sports.models import Court, Inventory, Sport


@login_required
def home(request):
    sports = Sport.objects.all()
    return render(request, 'Sports/home.html', {'sports': sports})


def sportsDetailView(request, id):
    sport = Sport.objects.get(id=id)
    context = {'sport': sport, 'courts': Court.objects.filter(sport=sport), 'inventories': Inventory.objects.filter(sport=sport)
               }
    return render(request, 'Sports/sport_detail.html', context)
