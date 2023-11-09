from django.contrib import admin
from .models import Booking, BookingType, BookingStatus
from  client.models import Client
# Register your models here.
admin.site.register(Booking)
admin.site.register(BookingType)
admin.site.register(BookingStatus)
admin.site.register(Client)