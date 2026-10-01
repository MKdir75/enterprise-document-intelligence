from django.db.models import Q

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Document
from .permissions import (
    CanCreateDocument,
    CanManageDocument,
)
from .serializers import DocumentSerializer


class DocumentListCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(
        self,
        request,
    ):
        user = request.user

        queryset = (
            Document.objects
            .select_related(
                "department",
                "uploaded_by",
            )
            .filter(
                is_active=True
            )
        )

        if user.role == "ADMIN":
            return queryset

        if user.department_id is None:
            return queryset.none()

        if user.role in {
            "MANAGER",
            "ANALYST",
            "USER",
        }:
            return queryset.filter(
                department_id=user.department_id
            )

        return queryset.none()

    def get(
        self,
        request,
    ):
        queryset = self.get_queryset(
            request
        )

        serializer = DocumentSerializer(
            queryset,
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
        permission = CanCreateDocument()

        if not permission.has_permission(
            request,
            self,
        ):
            return Response(
                {
                    "detail": permission.message
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = DocumentSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        department = serializer.validated_data[
            "department"
        ]

        if request.user.role != "ADMIN":

            if (
                request.user.department_id
                != department.id
            ):
                return Response(
                    {
                        "detail": (
                            "You can only upload "
                            "documents for your "
                            "own department."
                        )
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )

        document = serializer.save(
            uploaded_by=request.user
        )

        return Response(
            DocumentSerializer(
                document
            ).data,
            status=status.HTTP_201_CREATED,
        )


class DocumentDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(
        self,
        request,
        document_id,
    ):
        try:
            document = (
                Document.objects
                .select_related(
                    "department",
                    "uploaded_by",
                )
                .get(
                    id=document_id,
                    is_active=True,
                )
            )
        except Document.DoesNotExist:
            return None

        if request.user.role == "ADMIN":
            return document

        if (
            request.user.department_id
            != document.department_id
        ):
            return None

        return document

    def get(
        self,
        request,
        document_id,
    ):
        document = self.get_object(
            request,
            document_id,
        )

        if document is None:
            return Response(
                {
                    "detail": (
                        "Document not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = DocumentSerializer(
            document
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def patch(
        self,
        request,
        document_id,
    ):
        document = self.get_object(
            request,
            document_id,
        )

        if document is None:
            return Response(
                {
                    "detail": (
                        "Document not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        permission = CanManageDocument()

        if not permission.has_object_permission(
            request,
            self,
            document,
        ):
            return Response(
                {
                    "detail": permission.message
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = DocumentSerializer(
            document,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def delete(
        self,
        request,
        document_id,
    ):
        document = self.get_object(
            request,
            document_id,
        )

        if document is None:
            return Response(
                {
                    "detail": (
                        "Document not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        permission = CanManageDocument()

        if not permission.has_object_permission(
            request,
            self,
            document,
        ):
            return Response(
                {
                    "detail": permission.message
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        document.is_active = False

        document.save(
            update_fields=[
                "is_active",
                "updated_at",
            ]
        )

        return Response(
            {
                "message": (
                    "Document deleted successfully."
                )
            },
            status=status.HTTP_204_NO_CONTENT,
        )