from django.db import models
from supplier.models import Supplier
# Create your models here.
CATEGORY_CHOICES = (
    ('NA', 'National Newspaper'),
    ('IN', 'International Newspaper'),
    ('RN', 'Regional Newspaper'),
    ('JM', 'Journal/Magazine'),
    ('OT', 'Others'),
)


TYPE_CHOICES = (
    ('FR', 'Free Newspaper'),
    ('PD', 'Paid Newspaper'),
    ('OT', 'Others'),
)
# Create your models here.

class TourOverview (models.Model):
    tour_title = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    price = models.FloatField()
    operator = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=4, default="NA")
    n_type = models.CharField(choices=TYPE_CHOICES, max_length=4, default="FR")
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    phone2 = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200, null=True, blank=True)
    added_date = models.DateTimeField('date published', null=True, blank=True)

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



class RoomType (models.Model):
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
