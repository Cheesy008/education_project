from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UsersSerializers, UserDetailSerializer
from .serializers import (
    QuizSerializer,
    QuizDetailSerializer,
    QuestionSerializer,
    AnswerSerializer,
)
from main.models import (
    Quiz,
    Answer,
    Question
)


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

    # @action(methods=['get', 'post'], detail=True)
    # def create_answer(self, request, id=None):
    #     question = self.get_object()
    #     data = request.data
    #     data['question'] = question.id
    #     serializer = AnswerSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    detail_serializer_class = QuizDetailSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        return super().get_serializer_class()

    # def retrieve(self, request, *args, **kwargs):
    #     quiz = self.get_object()
    #     questions = Question.objects.filter(quiz=quiz)
    #     serializer = QuestionSerializer(questions, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def create(self, request, *args, **kwargs):
    #     message = request.data.pop('message_type')
    #
    #     if message == 'Create':
    #         event = request.data.pop('event')
    #         questions = event.pop('question')[0]
    #         answers = event.pop('answer')
    #         questions = Question.objects.create(**questions)
    #
    #         for answer in answers:
    #             questions.answer_set.create(**answer)
    #         quiz = Quiz.objects.create(**event, )

