from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from drf_writable_nested import WritableNestedModelSerializer

from main.models import Quiz, Question, Answer


class MyRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    role = serializers.ChoiceField(choices=get_user_model().ROLE_CHOICES, write_only=True, default=None)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.role = self.validated_data.get('role', '')
        user.save(update_fields=['username', 'first_name', 'last_name', 'role'])


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'age',
            'role',
        )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'age',
            'role',
        )


class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Answer
        fields = (
            'id',
            'question',
            'answer_text',
            'is_correct',
        )
        read_only_fields = ('question',)


class QuestionSerializer(WritableNestedModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'index',
            'quiz',
            'question_title',
            'answers',
        )
        read_only_fields = ('quiz',)


class QuizSerializer(WritableNestedModelSerializer):
    owner = UserDetailSerializer(read_only=True)
    owner_id = serializers.SerializerMethodField()
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'owner',
            'owner_id',
            'questions_count',
            'description',
            'test_completed',
            'created',
            'questions',
        )
        read_only_fields = ('questions_count', 'test_completed', )

    def get_owner_id(self, obj):
        owner_id = self.context['request'].user.id
        return owner_id















