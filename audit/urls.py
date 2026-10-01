from django.urls import path

from .views import (
    AuditLogCreateView,
    AuditLogListView,
)


urlpatterns = [
    path(
        "",
        AuditLogListView.as_view(),
        name="audit-log-list",
    ),

    path(
        "create/",
        AuditLogCreateView.as_view(),
        name="audit-log-create",
    ),
]