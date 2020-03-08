from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response

from .serializers import UsersSerializers

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UsersSerializers
#
#     @action(methods=['get'], detail=True, url_path='profile/current_user/', url_name='profile/current_user/')
#     def get_object(self):
#         pk = self.kwargs.get('pk')
#         if pk == 'current':
#             return self.request.user
#
#         return super(UserViewSet, self).get_object()
#


class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializers


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsersSerializers


@api_view(['GET'])
def get_current_user(request):
    serializer = UsersSerializers(request.user)
    return Response(serializer.data)






