from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from base.manager import BaseModelManager, BaseQuerySet


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+", null=True, blank=True
    )
    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+", null=True, blank=True
    )
    is_active = models.BooleanField(
        _("Is Instance Active"),
        default=True,
    )
    udf_1 = models.CharField(max_length=255, null=True, blank=True)
    udf_2 = models.CharField(max_length=255, null=True, blank=True)
    udf_3 = models.CharField(max_length=255, null=True, blank=True)
    objects = BaseModelManager.from_queryset(BaseQuerySet)()

    class Meta:
        abstract = True
