from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import (UserCreateSerializer,
                          UserListSerializer,
                          UserLoginSerializer)
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
