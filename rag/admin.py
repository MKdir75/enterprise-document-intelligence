from django.contrib import admin

from .models import (
    RAGQuery,
    RAGSource,
)


@admin.register(RAGQuery)
class RAGQueryAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "question",
        "created_at",
    ]

    search_fields = [
        "question",
        "answer",
        "user__username",
    ]


@admin.register(RAGSource)
class RAGSourceAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "query",
        "document",
        "chunk",
        "relevance_score",
        "created_at",
    ]

    list_filter = [
        "document",
    ]