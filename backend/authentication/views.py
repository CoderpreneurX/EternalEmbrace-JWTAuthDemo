from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile

class RegisterUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CreateUserProfileView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        data = self.request.data

        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.save()

        serializer.save(user=user)

        return serializer