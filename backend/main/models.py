from django.db import models
from django.contrib.auth import get_user_model

from users.models import Profile


class Quiz(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='quizzes',
        verbose_name='Создатель',
    )
    title = models.CharField(max_length=100, verbose_name='Название')
    questions_count = models.PositiveSmallIntegerField(default=0, verbose_name='Количество вопросов', null=True, blank=True)
    description = models.TextField(verbose_name='Описание теста')
    test_created = models.BooleanField(default=False, verbose_name='Завершено создание теста')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    index = models.SmallIntegerField(blank=True, null=True, default=0)
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE, verbose_name='Тест')
    question_title = models.TextField(verbose_name='Текст вопроса')

    def __str__(self):
        return self.question_title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    @property
    def answers(self):
        return self.answers.all()


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE, verbose_name='Текст вопроса')
    answer_text = models.TextField(verbose_name='Текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Правильный')

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class QuizRoom(models.Model):
    owner = models.ForeignKey(
        Profile,
        related_name='owners',
        on_delete=models.CASCADE,
        verbose_name='Создатель',
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name='Пользователь',
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Завершён',
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        null=True,
        related_name='quizzes',
        verbose_name='Тест',
    )

    def __str__(self):
        return f"Комната - {self.quiz.title}"

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class QuizResponse(models.Model):
    quiz_room = models.ForeignKey(
        QuizRoom,
        on_delete=models.CASCADE,
        null=True,
        related_name='quiz_responses',
        verbose_name='Комната',
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.PROTECT,
        verbose_name='Ответ',
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.PROTECT,
        verbose_name='Вопрос',
    )

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователя'



