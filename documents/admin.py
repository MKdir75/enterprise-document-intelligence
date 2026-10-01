from django.contrib import admin

from .models import (
    Document,
    DocumentChunk,
)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "title",
        "document_type",
        "department",
        "uploaded_by",
        "is_active",
        "created_at",
    ]

    list_filter = [
        "document_type",
        "department",
        "is_active",
    ]

    search_fields = [
        "title",
        "description",
    ]


@admin.register(DocumentChunk)
class DocumentChunkAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "document",
        "chunk_index",
        "token_count",
        "created_at",
    ]

    search_fields = [
        "content",
        "document__title",
    ]