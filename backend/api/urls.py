from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, CurrentUserView


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('profile/', CurrentUserView.as_view()),
]

urlpatterns += router.urls
