from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.utils.translation import gettext_lazy as _

from .models import User

@admin.register(User)
class UserAdmin(UserAdminBase):
    readonly_fields = ["username"]

    fieldsets = list(UserAdminBase.fieldsets) + [
        (_("Extra"), {"fields": ["bio", "avatar"]})
    ]