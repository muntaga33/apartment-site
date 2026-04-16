from django.db import migrations


def create_admin(apps, schema_editor):
    User = apps.get_model("auth", "User")

    username = "admin"
    email = "muntaga@hotmail.com"
    password = "admin12345"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )


def remove_admin(apps, schema_editor):
    User = apps.get_model("auth", "User")
    User.objects.filter(username="admin").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0012_apartmentimage"),
    ]

    operations = [
        migrations.RunPython(create_admin, remove_admin),
    ]