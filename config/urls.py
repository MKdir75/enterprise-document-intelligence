from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "api/auth/",
        include("accounts.urls"),
    ),

    path(
        "api/departments/",
        include("departments.urls"),
    ),

    path(
        "api/documents/",
        include("documents.urls"),
    ),

    path(
        "api/rag/",
        include("rag.urls"),
    ),

    path(
        "api/conversations/",
        include("conversations.urls"),
    ),

    path(
        "api/audit-logs/",
        include("audit.urls"),
    ),
]