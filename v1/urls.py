from django.urls import path

from v1.apis import (
    PlaceListAPIView,
    ActivityListAPIView,
    UserProfileAPIView,
    PlaceRetrieveAPIView,
    ActivityCategoryListAPIView,
    AreaTypeListAPIView,
    TransportTypeListAPIView,
    AtmosphereListAPIView,
    SpacingTypeListAPIView,
    GroupTypeListAPIView,
    FeedbackRetrieveUpdateAPIView,
    FeedbackListCreateAPIView,
    ActivityPlanListCreateAPIView,
    ActivityPlanRetrieveUpdateAPIView,
    SubscriptionCreateAPIView,
    AttachmentGroupListAPIView,
    AttachmentListAPIView,
    QAGroupListAPIView,
    QAItemListAPIView,
    BookmarkCreateAPIView,
    BookmarkRetrieveUpdateAPIView,
    EventListAPIView,
    CityListAPIView,
)


urlpatterns = [
    path("me/", UserProfileAPIView.as_view(), name="user-profile"),
    path("place/", PlaceListAPIView.as_view(), name="place-list"),
    path("place/<int:pk>/", PlaceRetrieveAPIView.as_view(), name="place-detail"),
    path("activity/", ActivityListAPIView.as_view(), name="activity-list"),
    path(
        "activity-category/",
        ActivityCategoryListAPIView.as_view(),
        name="activity-category-list",
    ),
    path("area-type/", AreaTypeListAPIView.as_view(), name="area-type-list"),
    path(
        "transport-type/",
        TransportTypeListAPIView.as_view(),
        name="transport-type-list",
    ),
    path("atmosphere/", AtmosphereListAPIView.as_view(), name="atmosphere-list"),
    path("spacing-type/", SpacingTypeListAPIView.as_view(), name="spacing-type-list"),
    path("group-type/", GroupTypeListAPIView.as_view(), name="group-type-list"),
    path("feedback/", FeedbackListCreateAPIView.as_view(), name="feedback-list-create"),
    path(
        "feedback/<int:pk>/",
        FeedbackRetrieveUpdateAPIView.as_view(),
        name="feedback-detail-update",
    ),
    path(
        "activity-plan/",
        ActivityPlanListCreateAPIView.as_view(),
        name="activity-plan-list-create",
    ),
    path(
        "activity-plan/<int:pk>/",
        ActivityPlanRetrieveUpdateAPIView.as_view(),
        name="activity-plan-detail-update",
    ),
    path(
        "subscription/", SubscriptionCreateAPIView.as_view(), name="subscription-create"
    ),
    path(
        "attachment-group/",
        AttachmentGroupListAPIView.as_view(),
        name="attachment-group-list",
    ),
    path(
        "attachment/",
        AttachmentListAPIView.as_view(),
        name="attachment-list",
    ),
    path(
        "qa-group/",
        QAGroupListAPIView.as_view(),
        name="qa-group-list",
    ),
    path(
        "qa-item/",
        QAItemListAPIView.as_view(),
        name="qa-item-list",
    ),
    path("bookmark/", BookmarkCreateAPIView.as_view(), name="bookmark-list-create"),
    path(
        "bookmark/<int:pk>",
        BookmarkRetrieveUpdateAPIView.as_view(),
        name="bookmark-details-update",
    ),
    path("event/", EventListAPIView.as_view(), name="event-list"),
    path("city/", CityListAPIView.as_view(), name="city-list"),
]
