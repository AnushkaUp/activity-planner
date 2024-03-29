from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import BookmarkModelSerializer
from v1.models import Bookmark


class BookmarkCreateAPIView(ListCreateAPIView):
    queryset = Bookmark.objects.filter()
    serializer_class = BookmarkModelSerializer
    ordering = ["-created_at"]
    search_fields = ["place__name", "user__first_name", "user__last_name"]

    def get_queryset(self):
        if self.request.method == "POST":
            return super().get_queryset()
        return super().get_queryset().filter_active(user=self.request.user)


class BookmarkRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Bookmark.objects.filter()
    serializer_class = BookmarkModelSerializer
