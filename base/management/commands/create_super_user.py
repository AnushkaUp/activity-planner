from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a super user with username: admin, password: admin"

    def handle(self, *args, **options):
        from django.contrib.auth.models import User
        from django.contrib.auth.hashers import make_password

        admin_user_name = settings.ADMIN_USER_NAME
        admin_user_password = settings.ADMIN_USER_PASSWORD
        if not User.objects.filter(username=admin_user_name).exists():
            User.objects.create_superuser(admin_user_name, password=admin_user_password)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Super user with username: {admin_user_name} created successfully"
                )
            )
        else:
            User.objects.filter(username=admin_user_name).update(
                password=make_password(admin_user_password),
                is_superuser=True,
                is_staff=True,
            )
            self.stdout.write(
                self.style.WARNING(
                    f"Super user with username: {admin_user_name} already exists and password updated successfully"
                )
            )
