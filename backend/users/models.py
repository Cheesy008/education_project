from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


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


# @receiver(post_save, sender=User)
# def add_user_to_public_group(sender, instance, created, **kwargs):
#     try:
#         if created:
#             instance.groups.add(Group.objects.get(name='Студенты'))
#     except Group.DoesNotExist:
#         pass


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


