from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from base.models import BaseModel
from v1.models import Place


User = get_user_model()


class ActivityPlan(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    plan_of = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="plans", null=True, blank=True
    )
    total_price = models.FloatField(null=True, blank=True)
    number_of_people = models.IntegerField(null=True, blank=True)
    joinies = models.ManyToManyField(
        User,
        related_name="joined_plans",
        blank=True,
        through="ActivityPlanJoin",
        through_fields=("activity_plan", "user"),
    )

    class Meta:
        verbose_name = _("Activity Plan")
        verbose_name_plural = _("Activity Plans")

    def save(self, *args, **kwargs) -> None:
        if not self.name:
            self.name = self.get_unique_name()
        return super().save(*args, **kwargs)

    def get_unique_name(self, count=0) -> str:
        name = (
            f"{self.plan_of.username} - {self.start_time} - {self.end_time} - {count}"
        )
        if not ActivityPlan.objects.filter(name=name).exists():
            return name
        return self.get_unique_name(count + 1)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ActivityPlanItem(BaseModel):
    activity_plan = models.ForeignKey(
        ActivityPlan,
        on_delete=models.PROTECT,
        related_name="lines",
    )
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    place = models.ForeignKey(Place, on_delete=models.PROTECT, related_name="+")
    price = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = _("Activity Plan Item")
        verbose_name_plural = _("Activity Plan Items")

    def __str__(self):
        return self.place.name + " - " + self.activity_plan.plan_of.first_name

    def __repr__(self):
        return self.place.name + " - " + self.activity_plan.plan_of.first_name

    def __unicode__(self):
        return self.place.name + " - " + self.activity_plan.plan_of.first_name


class ActivityPlanJoin(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_plan = models.ForeignKey(ActivityPlan, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(_("Is Accepted by Planner"), default=False)
    joining_request_date = models.DateTimeField(
        _("Joining Request Date"), null=True, blank=True
    )
    joining_accept_date = models.DateTimeField(
        _("Joining Acceptance Date"), null=True, blank=True
    )
    join_date = models.DateTimeField(
        _("Plan Joining Date of user"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Activity Plan Join")
        verbose_name_plural = _("Activity Plan Joins")

    def __str__(self):
        return self.user.username + " - " + self.activity_plan.name

    def __repr__(self):
        return self.user.username + " - " + self.activity_plan.name

    def __unicode__(self):
        return self.user.username + " - " + self.activity_plan.name
