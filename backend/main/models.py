from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    test_completed = models.BooleanField(default=False, verbose_name='Завершено создание теста')
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
    question = models.ForeignKey(Question,related_name='answers', on_delete=models.CASCADE, verbose_name='Текст вопроса')
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
        related_name='quizrooms',
        on_delete=models.CASCADE,
        verbose_name='Создатель',
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Завершён',
    )
    quiz_response = models.ForeignKey(
        'QuizResponse',
        on_delete=models.PROTECT,
    )


class QuizResponse(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        verbose_name='Пользователь',
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


@receiver(post_save, sender=Quiz)
def set_default_quiz(sender, instance, created, **kwargs):
    quiz = Quiz.objects.filter(id=instance.id)
    quiz.update(questions_count=instance.questions.filter(quiz=instance.pk).count())


@receiver(post_save, sender=Question)
def set_default(sender, instance, created, **kwargs):
    quiz = Quiz.objects.filter(id=instance.quiz.id)
    quiz.update(questions_count=instance.quiz.questions.filter(quiz=instance.quiz.pk).count())

