from django.db import models

# Create your models here.

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

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default="NA")
    o_type = models.CharField(choices=TYPE_CHOICES, max_length=2, default="FR")
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    phone2 = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=200, default="password0")
    confirm_password = models.CharField(max_length=200, default="password0")
    website = models.CharField(max_length=200, blank=True, null=True)
    no_of_newspapers = models.CharField(max_length=200)
    added_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.added_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    operator = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text