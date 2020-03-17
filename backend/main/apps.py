from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Раздел с тестами'

    def ready(self):
        from . import signals
