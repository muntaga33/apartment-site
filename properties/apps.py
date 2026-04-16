from django.apps import AppConfig


class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'

    def ready(self):
        import os
        if os.environ.get("RENDER") != "true":
            return

        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()

            username = "admin"
            email = "muntaga@hotmail.com"
            password = "admin12345"

            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username, email, password)
        except Exception:
            pass