from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    exclude = (
        "udf_1",
        "udf_2",
        "udf_3",
    )
    readonly_fields = (
        "created_by",
        "updated_by",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, "created_by", None) is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class BaseInlineAdmin(admin.StackedInline):
    exclude = (
        "udf_1",
        "udf_2",
        "udf_3",
    )
    readonly_fields = (
        "created_by",
        "updated_by",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)
