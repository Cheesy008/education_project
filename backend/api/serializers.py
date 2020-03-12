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


class QuestionSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        answers = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)
        for answer in answers:
            Answer.objects.create(**answer, question=question)
        return question

    # def update(self, instance, validated_data):
    #     answers = validated_data.pop('answers')
    #     instance.question_title = validated_data.get('question_title', instance.question_title)
    #     instance.save()
    #     keep_answers = []
    #     existing_ids = [a.id for a in instance.answers]
    #     for answer in answers:
    #         if 'id' in answer.keys():
    #             if Answer.objects.filter(id=answer['id']).exists():
    #                 a = Answer.objects.get(id=answer['id'])
    #                 a.answer_text = answer.get('answer_text', a.answer_text)
    #                 a.save()
    #                 keep_answers.append(a.id)
    #             else:
    #                 continue
    #         else:
    #             a = Answer.objects.create(**answer, question=instance)
    #             keep_answers.append(a.id)
    #
    #     for answer in instance.answers:
    #         if answer.id not in keep_answers:
    #             answer.delete()
    #
    #     return instance

    def update(self, instance, validated_data):
        instance.question_title = validated_data.get('question_title', instance.question_title)
        answers = validated_data.pop('answers')
        for answer in answers:
            a = Answer.objects.get(id=answer['id'])
            a.answer_text = validated_data.get('answer_text', a.answer_text)
            a.is_correct = validated_data.get('is_correct', a.is_correct)
            a.save()
        instance.save()
        return instance


class QuizSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Quiz
        fields = (
            'id',
            'owner',
            'title',
            'questions_count',
            'created',
        )

    def get_owner(self, obj):
        return obj.owner.user.username


class QuizDetailSerializer(WritableNestedModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    question = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = (
            'id',
            'owner',
            'title',
            'questions_count',
            'description',
            'test_completed',
            'created',
            'question',
            'answer',
        )














