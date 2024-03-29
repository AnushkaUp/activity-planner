from django.db import models
from django.contrib.auth.models import User
from v1.models import Place
from base.constants.profile import ProfileGenderChoices, ProfileRoleChoices
from .state import Country


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(
        max_length=255, null=True, blank=True, choices=ProfileRoleChoices.choices
    )
    gender = models.CharField(
        choices=ProfileGenderChoices.choices, max_length=255, null=True, blank=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, null=True, blank=True
    )
    title_for_staff = models.CharField(max_length=255, null=True, blank=True)
    employer = models.ForeignKey(
        Place, on_delete=models.PROTECT, related_name="staff", blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.user.username} Profile"
