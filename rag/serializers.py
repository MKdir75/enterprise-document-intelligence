from rest_framework import serializers

from .models import (
    RAGQuery,
    RAGSource,
)


class RAGSourceSerializer(
    serializers.ModelSerializer
):

    document_title = serializers.CharField(
        source="document.title",
        read_only=True,
    )

    class Meta:
        model = RAGSource

        fields = [
            "id",
            "document",
            "document_title",
            "chunk",
            "relevance_score",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]


class RAGQuerySerializer(
    serializers.ModelSerializer
):

    sources = RAGSourceSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = RAGQuery

        fields = [
            "id",
            "question",
            "answer",
            "sources",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "answer",
            "sources",
            "created_at",
        ]