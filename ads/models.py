from django.db import models

from django.conf import settings

class Ad(models.Model):
    AD_TYPE_CHOICES = [
        ('house_owner', 'House Owner'),
        ('renter', 'Renter'),
    ]
    
    ad_type = models.CharField(max_length=20, choices=AD_TYPE_CHOICES)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    mortgage_price = models.IntegerField(null=True, blank=True)
    rent_price = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=2000)

