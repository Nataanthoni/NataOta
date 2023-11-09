from django.db import models
import datetime
from django.utils import timezone
from django.utils.timezone import now
from client.models import Client
from supplier.models import Supplier
# Create your models here.

class BookingType(models.Model):
    type = models.CharField(max_length=10)
    def __str__(self):
        return self.type

class BookingStatus(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status


class Booking(models.Model):
    def get_last():
       return Client.objects.filter(pub_date__year=2023).order_by("-pub_date")

    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, default=get_last)
    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=1)
    source = models.CharField(max_length=200)
    budget = models.CharField(max_length=200)
    pax = models.CharField(max_length=10)
    safari_title = models.CharField(max_length=200)
    
    inquiry_date = models.DateTimeField('Inquired on', default=now, null=True)
    departure_date = models.DateTimeField('Departing on', default=now, null=True)
    
    description = models.TextField(max_length=5000, null=False, blank=False)
    comments = models.TextField(max_length=5000, null=False, blank=False)
    medical_restriction = models.TextField(max_length=1000, null=False, blank=False)

    starting_point = models.CharField(max_length=200)
    assigned_guides = models.CharField(max_length=200)
    ending_point = models.CharField(max_length=200)

    booking_status = models.ForeignKey(BookingStatus, default=1, on_delete=models.CASCADE, null=True, blank=True)
    booking_type = models.ForeignKey(BookingType, on_delete=models.CASCADE)

    price = models.FloatField()
    consultant = models.CharField(max_length=100, null=True, blank=True)
    paid_amount = models.FloatField(null=True, blank=True)
    balance = models.FloatField(null=True, blank=True)
    due_date = models.DateTimeField('date published', blank=False, null=True)

    def __str__(self):
        return self.safari_title


