from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, CreateUserProfileView, EditUserProfileView, RetrieveUserProfileView

urlpatterns = [
    path('auth/user/register/', RegisterUserView.as_view(), name='register-user'),
    path('auth/user/login/', TokenObtainPairView.as_view(), name="login-user"),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name="refresh-token"),
    path('auth/profile/register/', CreateUserProfileView.as_view(), name='create-user-profile'),
    path('auth/profile/edit/', EditUserProfileView.as_view(), name='edit-user-profile'),
    path('auth/profile/', RetrieveUserProfileView.as_view(), name='retrieve-user-profile'),
]