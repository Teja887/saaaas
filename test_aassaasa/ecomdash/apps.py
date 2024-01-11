from django.apps import AppConfig


class EcomdashConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ecomdash"

    def ready(self):
        import ecomdash.signals

        