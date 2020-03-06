from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import UsersSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializers


