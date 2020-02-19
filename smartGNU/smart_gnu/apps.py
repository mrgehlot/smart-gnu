from django.apps import AppConfig


class SmartGnuConfig(AppConfig):
    name = 'smart_gnu'

    def ready(self):
        from smart_gnu import signals