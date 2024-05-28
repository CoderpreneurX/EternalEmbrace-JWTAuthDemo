from django.urls import path
from .views import RegisterUserView, CreateUserProfileView

urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register-user'),
    path('auth/profile/register/', CreateUserProfileView.as_view(), name='create-user-profile'),
]