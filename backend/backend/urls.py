from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login-user'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]
