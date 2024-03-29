from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class NewsLetterSubscription(BaseModel):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = _("News Letter Subscription")
        verbose_name_plural = _("News Letter Subscriptions")

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email

    def __unicode__(self):
        return self.email
