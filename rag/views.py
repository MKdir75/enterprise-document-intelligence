from django.db.models import Q

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from documents.models import Document

from .models import RAGQuery
from .serializers import RAGQuerySerializer


class RAGQueryView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(
        self,
        request,
    ):
        question = request.data.get(
            "question"
        )

        if not question:
            return Response(
                {
                    "detail": (
                        "Question is required."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user

        documents = (
            Document.objects
            .filter(
                is_active=True
            )
            .select_related(
                "department"
            )
        )

        if user.role != "ADMIN":

            if user.department_id is None:
                documents = documents.none()

            else:
                documents = documents.filter(
                    department_id=(
                        user.department_id
                    )
                )

        query = RAGQuery.objects.create(
            user=user,
            question=question,
            answer=(
                "RAG workflow is not connected yet. "
                "Document retrieval foundation is ready."
            ),
        )

        serializer = RAGQuerySerializer(
            query
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class RAGQueryHistoryView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(
        self,
        request,
    ):
        queryset = RAGQuery.objects.filter(
            user=request.user
        )

        serializer = RAGQuerySerializer(
            queryset,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )