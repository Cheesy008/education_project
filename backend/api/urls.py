from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import (
    UserViewSet,
    CurrentUserView,
    QuestionViewSet,
    QuizViewSet,
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('questions', QuestionViewSet, basename='questions')
router.register('quizzes', QuizViewSet, basename='quizzes')


urlpatterns = [
    path('profile/', CurrentUserView.as_view(),)
]

urlpatterns += router.urls
