from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from base.models import BaseModel


class Event(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Status:
        UPCOMING = "Upcoming"
        ONGOING = "Ongoing"
        ENDED = "Ended"

    @property
    def status(self):
        if self.start_date > timezone.now():
            return self.Status.UPCOMING
        elif self.end_date < timezone.now():
            return self.Status.ENDED
        else:
            return self.Status.ONGOING
