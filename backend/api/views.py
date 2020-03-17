from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UsersSerializers, UserDetailSerializer
from .serializers import (
    QuizSerializer,
    QuestionSerializer,
    AnswerSerializer,
)
from main.models import (
    Quiz,
    Answer,
    Question
)
from .filters import QuizFilter


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


# @api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticatedOrReadOnly,))
# def quizzes(request):
#     if request.method == 'POST':
#         serializer = QuizSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         quizzes_list = Quiz.objects.all()
#         serializer = QuizSerializer(quizzes_list, many=True)
#         return Response(serializer.data)


# class QuizViewSet(viewsets.ModelViewSet):
#     queryset = Quiz.objects.all()
#     serializer_classes = {
#         'quiz_list': QuizSerializer,
#         'create_quiz': QuizDetailSerializer,
#     }
#
#     default_serializer_class = QuizDetailSerializer
#
#     def get_serializer_class(self):
#         return self.serializer_classes.get(self.action, self.default_serializer_class)
#
#     @action(methods=['get'], detail=False, url_name='', url_path='',
#             permission_classes=(AllowAny,))
#     def quiz_list(self, request, *args, **kwargs):
#         quiz = Quiz.objects.all()
#         serializer = QuizSerializer(quiz, many=True)
#         return Response(serializer.data)
#
#     @action(methods=['get', 'post'], detail=True, url_name='create', url_path='create',
#             permission_classes=(IsAuthenticated,))
#     def create_quiz(self, request, *args, **kwargs):
#         serializer = QuizDetailSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'

    @action(methods=['get'], detail=True, url_path='answers')
    def answers_list(self, request, id=None):
        question = self.get_object()
        answers = Answer.objects.filter(question=question)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering = ('created',)
    filterset_class = QuizFilter

    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        req = serializer.context['request']
        serializer.save(owner=req.user)
