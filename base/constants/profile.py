from django.db import models
from django.utils.translation import gettext_lazy as _


class ProfileRoleChoices(models.TextChoices):
    PUBLIC_USER = "public_user", _("User")
    VENDOR = "vendor", _("Vendor")
    ADMIN = "admin", _("Admin")
    STAFF = "staff", _("Staff")
    PLACE_STAFF = "place_staff", _("Place Staff")


class ProfileGenderChoices(models.TextChoices):
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")
    OTHER = "other", _("Other")
