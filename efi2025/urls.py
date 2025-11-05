from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('aerolineas/', include('aerolineas.urls')),

    # API REST
    path('api/', include('aerolineas.api.urls')),

    # Rutas JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
