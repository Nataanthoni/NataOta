from django.utils import timezone
from django.utils.timezone import now
from django.db import models

# Create your models here.

class Client(models.Model):

    USA = "FR"
    GERMANY = "DE"
    CANADA = "CA"
    SENIOR = "SR"
    GRADUATE = "GR"
    OTHER = "OT"
    CLIENT_COUNTRY_CHOICES = [
        (USA, "Unites States of America"),
        (GERMANY, "Germany"),
        (CANADA, "Canada"),
        (SENIOR, "Senior"),
        (GRADUATE, "Graduate"),
        (OTHER, "Other")
    ]
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=20)
    client_dob = models.DateField(max_length=20)
    client_email = models.CharField(max_length=200)
    client_country = models.CharField(
        max_length=2,
        choices=CLIENT_COUNTRY_CHOICES,
        default=OTHER,
    )
    pub_date = models.DateTimeField('Added on', default=now, null=True)
    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}

    def __str__(self):
        return self.client_name


