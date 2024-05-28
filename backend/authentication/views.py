from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class RegisterUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()