from django.urls import path, include
from hello.views.Vehicle import VehicleViewSet
from rest_framework import routers


urlpatterns = [
    path('vehicle/', VehicleViewSet.as_view({'get': 'list'}), name='vehicle'),
]