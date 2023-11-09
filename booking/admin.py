from django.contrib import admin
from .models import Booking, BookingType, BookingStatus
from supplier.models import Choice
# Register your models here.
admin.site.register(Booking)
admin.site.register(BookingType)
admin.site.register(BookingStatus)