from django.urls import path
from .views import RegisterUserView, CreateUserProfileView, EditUserProfileView

urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register-user'),
    path('auth/profile/register/', CreateUserProfileView.as_view(), name='create-user-profile'),
    path('auth/profile/edit/', EditUserProfileView.as_view(), name='edit-user-profile'),
]