from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleViewset(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    