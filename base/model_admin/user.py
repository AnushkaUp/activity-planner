from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from base.models.profile import Profile


User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0
    min_num = 1


class UserModelAdmin(UserAdmin):
    inlines = [ProfileInline]
