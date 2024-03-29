from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from base.models import BaseModel, State
from v1.constants import AttachmentTypeChoices, AttachmentMimeType, PlaceShiftChoices
from v1.models import Event


class AreaType(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Area Type")
        verbose_name_plural = _("Area Types")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


class GroupType(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Group Type")
        verbose_name_plural = _("Group Types")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


class TransPortType(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Transport Type")
        verbose_name_plural = _("Transport Types")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Atmosphere(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Atmosphere")
        verbose_name_plural = _("Atmospheres")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ActivityCategory(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Activity Category")
        verbose_name_plural = _("Activity Categories")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Activity(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    average_price = models.FloatField(_("Average Price"), null=True, blank=True)
    average_time_spent = models.FloatField(
        _("Average Price Spent"), null=True, blank=True
    )
    category = models.ForeignKey(ActivityCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activity")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


class SpacingType(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Spacing Type")
        verbose_name_plural = _("Spacing Types")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Place(BaseModel):
    name = models.CharField(_("Title"), max_length=255)
    description = models.TextField(null=True, blank=True)
    area_type = models.ManyToManyField(
        AreaType,
        related_name="places",
    )
    group_type = models.ManyToManyField(
        GroupType,
        related_name="places",
    )
    min_age = models.IntegerField(null=True, blank=True)
    max_age = models.IntegerField(null=True, blank=True)
    available_transport = models.ManyToManyField(
        TransPortType,
        related_name="places",
    )
    atmosphere = models.ManyToManyField(
        Atmosphere,
        related_name="places",
    )
    open_at = models.TimeField(null=True, blank=True)
    close_at = models.TimeField(null=True, blank=True)
    activity = models.ManyToManyField(
        Activity,
        related_name="places",
    )
    spacing = models.ForeignKey(
        SpacingType, on_delete=models.PROTECT, null=True, blank=True
    )
    max_price = models.FloatField(null=True, blank=True)
    min_price = models.FloatField(null=True, blank=True)
    average_price = models.FloatField(null=True, blank=True)
    average_time_spent = models.FloatField(null=True, blank=True)
    preferred_shift = models.CharField(
        max_length=255, null=True, blank=True, choices=PlaceShiftChoices.choices
    )
    extra = models.JSONField(_("Extra Info"), null=True, blank=True)

    class Meta:
        verbose_name = _("Place")
        verbose_name_plural = _("Places")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


User = get_user_model()


class Feedback(BaseModel):
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    place = models.ForeignKey(Place, on_delete=models.PROTECT, null=True, blank=True)
    rating = models.FloatField(_("Rating"), null=True, blank=True)
    comment = models.TextField(_("Comment"), null=True, blank=True)
    edited = models.BooleanField(_("Is Comment Edited"), default=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")

    def save(self, *args, **kwargs):
        if not self.id:
            self.owner = self.created_by
        super(Feedback, self).save(*args, **kwargs)

    def __str__(self):
        return (
            (self.place.name if self.place else self.parent.place.name)
            + " by "
            + self.owner.username
        )

    def __repr__(self):
        return (
            (self.place.name if self.place else self.parent.place.name)
            + " by "
            + self.owner.username
        )

    def __unicode__(self):
        return (
            (self.place.name if self.place else self.parent.place.name)
            + " by "
            + self.owner.name
        )


class MenuCategory(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Menu Category")
        verbose_name_plural = _("Menu Categories")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Menu(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(_("Price"))
    place = models.ForeignKey(
        Place, on_delete=models.PROTECT, null=True, blank=True, related_name="menu"
    )
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="menu",
    )

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class AttachmentGroup(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Attachment Group")
        verbose_name_plural = _("Attachment Groups")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Attachment(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="attachments", null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.PROTECT, null=True, blank=True)
    feedback = models.ForeignKey(
        Feedback, on_delete=models.PROTECT, null=True, blank=True
    )
    transport_type = models.ForeignKey(
        TransPortType,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="icons",
    )
    activity = models.ForeignKey(
        Activity, on_delete=models.PROTECT, null=True, blank=True, related_name="icons"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="profile_pics",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="attachments",
    )
    file_type = models.CharField(
        max_length=255, null=True, blank=True, choices=AttachmentTypeChoices.choices
    )
    mime_type = models.CharField(
        max_length=255, null=True, blank=True, choices=AttachmentMimeType.choices
    )
    group = models.ForeignKey(
        AttachmentGroup,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="attachments",
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="attachments",
    )
    group_type = models.ForeignKey(
        GroupType,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="icons",
    )
    atmosphere = models.ForeignKey(
        Atmosphere,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="icons",
    )

    class Meta:
        verbose_name = _("Attachment")
        verbose_name_plural = _("Attachments")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Address(BaseModel):
    street1 = models.CharField(max_length=255, null=True, blank=True)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    street3 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.PROTECT, related_name="addresses")
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name="addresses")
    event = models.ForeignKey(
        Event, on_delete=models.PROTECT, null=True, blank=True, related_name="addresses"
    )
    contact_number = models.CharField(
        _("Contact Number"), max_length=20, null=True, blank=True
    )
    contact_email = models.EmailField(_("Email"), null=True, blank=True)
    site_url = models.URLField(_("External URL"), null=True, blank=True)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")


class QAGroup(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Q&A Group")
        verbose_name_plural = _("Q&A Groups")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class QAItem(BaseModel):
    question = models.TextField()
    answer = models.TextField()
    group = models.ForeignKey(
        QAGroup, on_delete=models.CASCADE, null=True, blank=True, related_name="items"
    )
    place = models.ForeignKey(Place, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = _("Q&A Item")
        verbose_name_plural = _("Q&A Items")

    def __str__(self):
        return self.question

    def __repr__(self):
        return self.question


class Bookmark(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="bookmarks"
    )
    place = models.ForeignKey(
        Place, on_delete=models.PROTECT, null=True, blank=True, related_name="bookmarks"
    )

    class Meta:
        verbose_name = _("Bookmark")
        verbose_name_plural = _("Bookmarks")

    def __str__(self):
        return self.user.username + self.place.name

    def __repr__(self):
        return self.user.username + self.place.name
