from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Profile

class ProfileSerializer (ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'gender']