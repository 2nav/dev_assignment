from django.contrib import admin

from Sports.models import Booking, Court, Inventory, Slot, Sport

admin.site.register(Sport)
admin.site.register(Court)
admin.site.register(Inventory)
admin.site.register(Slot)
admin.site.register(Booking)
