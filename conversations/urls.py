from django.urls import path

from .views import (
    ConversationDetailView,
    ConversationListCreateView,
    MessageCreateView,
)


urlpatterns = [
    path(
        "",
        ConversationListCreateView.as_view(),
        name="conversation-list-create",
    ),

    path(
        "<int:conversation_id>/",
        ConversationDetailView.as_view(),
        name="conversation-detail",
    ),

    path(
        "<int:conversation_id>/messages/",
        MessageCreateView.as_view(),
        name="message-create",
    ),
]