from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Quiz(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    questions_count = models.PositiveSmallIntegerField(default=0, verbose_name='Количество вопросов')
    description = models.TextField(verbose_name='Описание теста')
    score = models.PositiveSmallIntegerField(default=0, verbose_name='Количество баллов')
    completed = models.BooleanField(default=False, verbose_name='Завершен')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тест')
    question_title = models.TextField(verbose_name='Текст вопроса')

    def __str__(self):
        return self.question_title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Текст вопроса')
    answer_text = models.TextField(verbose_name='Текст вопроса')
    is_correct = models.BooleanField(default=False, verbose_name='Правильный')

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


@receiver(post_save, sender=Quiz)
def set_default_quiz(sender, instance, created, **kwargs):
    quiz = Quiz.objects.get(id=instance.id)
    quiz.update(questions_count=instance.quiz.question_set.filter(quiz=instance.quiz.pk).count())


@receiver(post_save, sender=Question)
def set_default(sender, instance, created, **kwargs):
    quiz = Quiz.objects.get(id=instance.quiz.pk)
    quiz.update(questions_count=instance.quiz.question_set.filter(quiz=instance.quiz.pk).count())


