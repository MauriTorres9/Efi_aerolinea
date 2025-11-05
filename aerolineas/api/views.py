from rest_framework import viewsets, permissions, filters
from aerolineas.models import Vuelo, Pasajero
from .serializers import VueloSerializer, PasajeroSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Solo los administradores pueden crear, editar o eliminar vuelos.
    Los demás solo pueden ver.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
    
class VueloViewSet(viewsets.ModelViewSet):
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['origen', 'destino', 'fecha_salida']

class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer
    permission_classes = [permissions.IsAuthenticated]
