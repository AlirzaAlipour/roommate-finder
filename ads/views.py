from rest_framework.viewsets import ModelViewSet
from .models import Ad
from .serializers import AdSerializer

class AdViewSet (ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer