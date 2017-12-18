from .serializers import UserCreateSerializer, UserListSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import (IsAuthenticated,
                                        AllowAny,
                                        IsAdminUser,
                                        IsAuthenticatedOrReadOnly
                                        )

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
