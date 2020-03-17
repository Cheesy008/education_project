from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = 'Раздел с профилями'

    def ready(self):
        from . import signals
