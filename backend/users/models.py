from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_STUDENT = 'ST'
    ROLE_TEACHER = 'TE'
    ROLE_CHOICES = (
        (ROLE_STUDENT, 'Студент'),
        (ROLE_TEACHER, 'Учитель')
    )
    age = models.IntegerField(default=0, null=True, blank=True)
    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default=ROLE_CHOICES[0][1],
    )


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    quiz = models.ManyToManyField(
        to='main.Quiz',
        blank=True,
        verbose_name='Тест',
    )
    is_anonymous = models.BooleanField(
        default=False,
        verbose_name='Незарегистрирован'
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'





