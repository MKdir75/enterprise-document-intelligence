from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAdmin

from .models import AuditLog
from .serializers import AuditLogSerializer


class AuditLogListView(APIView):

    permission_classes = [
        IsAdmin,
    ]

    def get(
        self,
        request,
    ):
        logs = (
            AuditLog.objects
            .select_related(
                "user"
            )
            .all()
        )

        serializer = AuditLogSerializer(
            logs,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class AuditLogCreateView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(
        self,
        request,
    ):
        serializer = AuditLogSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        log = serializer.save(
            user=request.user
        )

        return Response(
            AuditLogSerializer(
                log
            ).data,
            status=status.HTTP_201_CREATED,
        )