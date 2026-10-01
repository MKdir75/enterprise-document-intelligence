from django.conf import settings
from django.db import models


class RAGQuery(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rag_queries",
    )

    question = models.TextField()

    answer = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return (
            f"RAG Query #{self.id} "
            f"by {self.user.username}"
        )


class RAGSource(models.Model):

    query = models.ForeignKey(
        RAGQuery,
        on_delete=models.CASCADE,
        related_name="sources",
    )

    document = models.ForeignKey(
        "documents.Document",
        on_delete=models.CASCADE,
        related_name="rag_sources",
    )

    chunk = models.ForeignKey(
        "documents.DocumentChunk",
        on_delete=models.CASCADE,
        related_name="rag_sources",
        null=True,
        blank=True,
    )

    relevance_score = models.FloatField(
        default=0.0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return (
            f"{self.query_id} -> "
            f"{self.document.title}"
        )