from rest_framework import serializers

from .models import Document, DocumentChunk


class DocumentChunkSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = DocumentChunk

        fields = [
            "id",
            "document",
            "chunk_index",
            "content",
            "token_count",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]


class DocumentSerializer(
    serializers.ModelSerializer
):

    uploaded_by_name = serializers.CharField(
        source="uploaded_by.username",
        read_only=True,
    )

    department_name = serializers.CharField(
        source="department.name",
        read_only=True,
    )

    chunk_count = serializers.IntegerField(
        source="chunks.count",
        read_only=True,
    )

    class Meta:
        model = Document

        fields = [
            "id",
            "title",
            "description",
            "file",
            "document_type",
            "department",
            "department_name",
            "uploaded_by",
            "uploaded_by_name",
            "is_active",
            "chunk_count",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "uploaded_by",
            "uploaded_by_name",
            "department_name",
            "chunk_count",
            "created_at",
            "updated_at",
        ]