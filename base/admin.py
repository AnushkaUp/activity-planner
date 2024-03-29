from django.contrib import admin
from django.contrib.auth import get_user_model
from base.model_admin.user import UserModelAdmin

from base.models import Country, State, City
from base.models.profile import Profile

User = get_user_model()
# Register your models here.
admin.site.site_header = "Activity Planner Admin"
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserModelAdmin)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
