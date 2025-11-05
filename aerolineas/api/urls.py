from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VueloViewSet, PasajeroViewSet

router = DefaultRouter()
router.register(r'vuelos', VueloViewSet, basename='vuelos')
router.register(r'pasajeros', PasajeroViewSet, basename='pasajeros')

urlpatterns = [
    path('', include(router.urls)),
]
