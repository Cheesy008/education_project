from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import UsersSerializers, UserDetailSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_classes = {
        'list': UsersSerializers,
        'retrieve': UserDetailSerializer,
    }
    default_serializer_class = UsersSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class CurrentUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)






