from django.db import models
from django.conf import settings


class Profile (models.Model):
    GENDER_CHOICES = [
        ("female", "Female"),
        ("male", "Male"),
        ("other", "Other"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)