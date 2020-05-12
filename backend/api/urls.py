from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import (
    UserViewSet,
    CurrentUserView,
    QuestionViewSet,
    QuizViewSet,
    QuizPassingViewSet,
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('questions', QuestionViewSet, basename='questions')
router.register('quizzes', QuizViewSet, basename='quizzes')
router.register('quiz_passing', QuizPassingViewSet, basename='quiz_passing')


urlpatterns = [
    path('profile/', CurrentUserView.as_view(),)
]

urlpatterns += router.urls
