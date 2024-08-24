from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Ad

class AdSerializer (ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'ad_type', 'user', 'location', 'mortgage_price', 'rent_price', 'description']