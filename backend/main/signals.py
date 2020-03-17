from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Quiz, Question


@receiver(post_save, sender=Quiz)
def set_default_quiz(sender, instance, created, **kwargs):
    quiz = Quiz.objects.filter(id=instance.id)
    quiz.update(questions_count=instance.questions.filter(quiz=instance.pk).count())


@receiver(post_save, sender=Question)
def set_default(sender, instance, created, **kwargs):
    quiz = Quiz.objects.filter(id=instance.quiz.id)
    quiz.update(questions_count=instance.quiz.questions.filter(quiz=instance.quiz.pk).count())
