from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAdmin

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentListCreateView(APIView):

    permission_classes = [
        IsAdmin,
    ]

    def get(
        self,
        request,
    ):
        departments = Department.objects.all()

        serializer = DepartmentSerializer(
            departments,
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
        serializer = DepartmentSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        department = serializer.save()

        return Response(
            DepartmentSerializer(
                department
            ).data,
            status=status.HTTP_201_CREATED,
        )


class DepartmentDetailView(APIView):

    permission_classes = [
        IsAdmin,
    ]

    def get_object(
        self,
        department_id,
    ):
        try:
            return Department.objects.get(
                id=department_id
            )
        except Department.DoesNotExist:
            return None

    def get(
        self,
        request,
        department_id,
    ):
        department = self.get_object(
            department_id
        )

        if department is None:
            return Response(
                {
                    "detail": (
                        "Department not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = DepartmentSerializer(
            department
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def patch(
        self,
        request,
        department_id,
    ):
        department = self.get_object(
            department_id
        )

        if department is None:
            return Response(
                {
                    "detail": (
                        "Department not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = DepartmentSerializer(
            department,
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
        department_id,
    ):
        department = self.get_object(
            department_id
        )

        if department is None:
            return Response(
                {
                    "detail": (
                        "Department not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        department.delete()

        return Response(
            {
                "message": (
                    "Department deleted successfully."
                )
            },
            status=status.HTTP_204_NO_CONTENT,
        )