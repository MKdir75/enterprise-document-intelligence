from django.contrib import admin

from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "action",
        "resource_type",
        "resource_id",
        "created_at",
    ]

    list_filter = [
        "action",
        "resource_type",
        "created_at",
    ]

    search_fields = [
        "description",
        "resource_type",
        "resource_id",
        "user__username",
    ]

    readonly_fields = [
        "created_at",
    ]