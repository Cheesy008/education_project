from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# @receiver(post_save, sender=User)
# def add_user_to_public_group(sender, instance, created, **kwargs):
#     try:
#         if created:
#             instance.groups.add(Group.objects.get(name='Студенты'))
#     except Group.DoesNotExist:
#         pass

