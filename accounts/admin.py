from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = [
        "id",
        "username",
        "email",
        "role",
        "department",
        "is_active",
        "is_staff",
    ]

    list_filter = [
        "role",
        "department",
        "is_active",
        "is_staff",
    ]

    search_fields = [
        "username",
        "email",
        "first_name",
        "last_name",
    ]

    fieldsets = UserAdmin.fieldsets + (
        (
            "Enterprise Information",
            {
                "fields": (
                    "role",
                    "department",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Enterprise Information",
            {
                "fields": (
                    "email",
                    "role",
                    "department",
                )
            },
        ),
    )