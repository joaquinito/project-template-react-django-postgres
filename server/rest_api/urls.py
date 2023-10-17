from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_api import views

# This creates the REST API endpoints for the Viewset-based view classes.
router = DefaultRouter()
router.register('vehicles', views.VehicleViewset)

app_name = 'rest_api'

urlpatterns = [
    path('', include(router.urls)),
]