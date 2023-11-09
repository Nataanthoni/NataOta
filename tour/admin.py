from django.contrib import admin
from .models import TourOverview, Itinerary, Inclusion, RoomType, Photo, Pricing, Property
# Register your models here.
admin.site.register(TourOverview)
admin.site.register(Itinerary)
admin.site.register(Photo)
admin.site.register(Inclusion)
admin.site.register(RoomType)
admin.site.register(Pricing)
admin.site.register(Property)
