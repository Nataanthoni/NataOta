from django.contrib import admin
from .models import Overview, Itinerary, Inclusion, Room_Type, Photo, Pricing, Property
# Register your models here.
admin.site.register(Overview)
admin.site.register(Itinerary)
admin.site.register(Photo)
admin.site.register(Inclusion)
admin.site.register(Room_Type)
admin.site.register(Pricing)
admin.site.register(Property)
