import django.utils
from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Court(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Slot(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    timeStart = models.DateTimeField()
    timeEnd = models.DateTimeField()
    available = models.BooleanField(default=False)


class Booking(models.Model):
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
    status = models.BooleanField()
    bookingDate = models.DateField(default=django.utils.timezone.now())
    bookingTime = models.DateTimeField(default=django.utils.timezone.now())
