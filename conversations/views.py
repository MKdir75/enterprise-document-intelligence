from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    Conversation,
    Message,
)
from .serializers import (
    ConversationSerializer,
    MessageSerializer,
)


class ConversationListCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(
        self,
        request,
    ):
        conversations = (
            Conversation.objects
            .filter(
                user=request.user
            )
            .prefetch_related(
                "messages"
            )
        )

        serializer = ConversationSerializer(
            conversations,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(
        self,
        request,
    ):
        serializer = ConversationSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        conversation = serializer.save(
            user=request.user
        )

        return Response(
            ConversationSerializer(
                conversation
            ).data,
            status=status.HTTP_201_CREATED,
        )


class ConversationDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(
        self,
        request,
        conversation_id,
    ):
        try:
            return (
                Conversation.objects
                .prefetch_related(
                    "messages"
                )
                .get(
                    id=conversation_id,
                    user=request.user,
                )
            )
        except Conversation.DoesNotExist:
            return None

    def get(
        self,
        request,
        conversation_id,
    ):
        conversation = self.get_object(
            request,
            conversation_id,
        )

        if conversation is None:
            return Response(
                {
                    "detail": (
                        "Conversation not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ConversationSerializer(
            conversation
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class MessageCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(
        self,
        request,
        conversation_id,
    ):
        try:
            conversation = (
                Conversation.objects.get(
                    id=conversation_id,
                    user=request.user,
                )
            )
        except Conversation.DoesNotExist:
            return Response(
                {
                    "detail": (
                        "Conversation not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MessageSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        message = serializer.save(
            conversation=conversation
        )

        return Response(
            MessageSerializer(
                message
            ).data,
            status=status.HTTP_201_CREATED,
        )