from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserDetail, UserList, get_current_user


# router = SimpleRouter()
# router.register('users', UserViewSet, basename='users')
#
# urlpatterns = router.urls

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('profile/', get_current_user),
]
