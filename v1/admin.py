from django.contrib import admin

from base.model_admin import BaseModelAdmin, BaseInlineAdmin
from v1.models import (
    Place,
    AreaType,
    GroupType,
    TransPortType,
    Attachment,
    Address,
    SpacingType,
    Activity,
    ActivityCategory,
    Atmosphere,
    Feedback,
    ActivityPlan,
    ActivityPlanItem,
    AttachmentGroup,
    QAGroup,
    QAItem,
    Bookmark,
    Menu,
    MenuCategory,
)

# Register your models here.

admin.site.register(AreaType, BaseModelAdmin)
admin.site.register(GroupType, BaseModelAdmin)
admin.site.register(TransPortType, BaseModelAdmin)
admin.site.register(Attachment, BaseModelAdmin)
admin.site.register(Address, BaseModelAdmin)
admin.site.register(SpacingType, BaseModelAdmin)
admin.site.register(Activity, BaseModelAdmin)
admin.site.register(ActivityCategory, BaseModelAdmin)
admin.site.register(Atmosphere, BaseModelAdmin)
admin.site.register(AttachmentGroup, BaseModelAdmin)
admin.site.register(QAGroup, BaseModelAdmin)
admin.site.register(QAItem, BaseModelAdmin)


class AddressInlineAdmin(BaseInlineAdmin):
    model = Address
    extra = 0
    min_num = 1


class PlaceAttachmentInlineAdmin(BaseInlineAdmin):
    exclude = ("feedback",)
    model = Attachment
    extra = 0


class PlaceModelAdmin(BaseModelAdmin):
    filter_horizontal = (
        "area_type",
        "group_type",
        "available_transport",
        # "spacing",
        "activity",
        "atmosphere",
    )
    inlines = (
        AddressInlineAdmin,
        PlaceAttachmentInlineAdmin,
    )


admin.site.register(Place, PlaceModelAdmin)


class FeedbackAttachmentInlineAdmin(BaseInlineAdmin):
    exclude = ("place",)
    model = Attachment
    extra = 0


class FeedbackModelAdmin(BaseModelAdmin):
    inlines = (FeedbackAttachmentInlineAdmin,)


admin.site.register(Feedback, FeedbackModelAdmin)


class ActivityPlanItemInlineAdmin(BaseInlineAdmin):
    model = ActivityPlanItem
    extra = 0
    min_num = 1


class ActivityPlanModelAdmin(BaseModelAdmin):
    inlines = (ActivityPlanItemInlineAdmin,)


admin.site.register(ActivityPlan, ActivityPlanModelAdmin)
admin.site.register(Bookmark, BaseModelAdmin)
admin.site.register(Menu, BaseModelAdmin)
admin.site.register(MenuCategory, BaseModelAdmin)
