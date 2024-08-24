from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AdViewSet

router = DefaultRouter()
router.register(r'ads' ,AdViewSet)




urlpatterns = [
    path('', include(router.urls)),
]