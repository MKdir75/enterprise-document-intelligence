from django.urls import path

from .views import (
    RAGQueryHistoryView,
    RAGQueryView,
)


urlpatterns = [
    path(
        "query/",
        RAGQueryView.as_view(),
        name="rag-query",
    ),

    path(
        "history/",
        RAGQueryHistoryView.as_view(),
        name="rag-history",
    ),
]