from django.utils import timezone
from django.utils.timezone import now
from django.db import models
import datetime
from supplier.models import Supplier
# Create your models here.
GROUP_TYPE = (
    ('GP', 'Group'),
    ('BT', 'Both'),
    ('PR', 'Private'),
)
GUIDE_TYPE = (
    ('PG', 'Partially Guided'),
    ('SG', 'Self Guided'),
    ('FG', 'Fully Guided'),
)

SINGLE_SUPPLEMENT = (
    ('NO', 'No Single Supplement'),
    ('YE', 'Mandatory Single Supplement')
)

INSTANT_BOOKING = (
    ('NO', 'No Instant Bookingt'),
    ('YE', 'Instant Booking')
)

PHYSICAL_RATING = (
    ('RE', 'Relaxing'),
    ('EA', 'Easy'),
    ('MO', 'Moderate'),
    ('SE', 'Serious'),
    ('HP', 'Heart pumping'),
)

TOUR_STATUS = (
    ('LV', 'Live'),
    ('DE', 'Deactivated'),
    ('PE', 'Pending'),
)
# Create your models here.

class Overview (models.Model):
    tour_title = models.CharField(max_length=200)

    operator = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)

    tour_code = models.CharField(max_length=200)
    tour_days = models.CharField(max_length=200)

    group_type = models.CharField(choices=GROUP_TYPE, max_length=2, default="PR")
    guide_type = models.CharField(choices=GUIDE_TYPE, max_length=2, default="FG")

    website_link = models.CharField(max_length=200, null=True, blank=True)
    
    single_supplement = models.CharField(choices=SINGLE_SUPPLEMENT, max_length=2, default="NO")
    instant_bookability = models.CharField(choices=INSTANT_BOOKING, max_length=2, default="YE")
    physical_rating = models.CharField(choices=PHYSICAL_RATING, max_length=2, default="SE")

    introduction = models.CharField(max_length=1200, null=True, blank=True)
    added_date = models.DateField('Added date', null=True, blank=True)

    class Meta:
        verbose_name_plural = ("       Overview")

    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.added_date >= timezone.now() - datetime.timedelta(days=1)


class Itinerary (models.Model):
    

    class Meta:
        verbose_name_plural = ("      Itineraries")

    def __str__(self):
        return self.name


class Photo (models.Model):
    class Meta:
        verbose_name_plural = ("     Photos")
    def __str__(self):
        return self.name



class Inclusion (models.Model):
    class Meta:
        verbose_name_plural = ("    Inclusions")
    def __str__(self):
        return self.name



class Room_Type (models.Model):
    class Meta:
        verbose_name_plural = ("   Room Types")
    def __str__(self):
        return self.name



class Pricing(models.Model):
    

    class Meta:
        verbose_name_plural = ("  Pricing")

    def __str__(self):
        return self.name


class Property (models.Model):
    

    class Meta:
        verbose_name_plural = (" Properties")

    def __str__(self):
        return self.name
