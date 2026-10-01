from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .permissions import IsAdmin
from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    UserRoleUpdateSerializer,
    UserSerializer,
)


class RegisterView(APIView):

    permission_classes = [
        AllowAny,
    ]

    def post(
        self,
        request,
    ):
        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.save()

        return Response(
            {
                "message": (
                    "User registered successfully."
                ),
                "user": UserSerializer(
                    user
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):

    permission_classes = [
        AllowAny,
    ]

    def post(
        self,
        request,
    ):
        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.validated_data[
            "user"
        ]

        refresh = RefreshToken.for_user(
            user
        )

        return Response(
            {
                "message": "Login successful.",

                "refresh": str(refresh),

                "access": str(
                    refresh.access_token
                ),

                "user": UserSerializer(
                    user
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class MeView(APIView):

    def get(
        self,
        request,
    ):
        serializer = UserSerializer(
            request.user
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class UserListView(APIView):

    permission_classes = [
        IsAdmin,
    ]

    def get(
        self,
        request,
    ):
        users = User.objects.select_related(
            "department"
        ).all()

        serializer = UserSerializer(
            users,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class UserRoleUpdateView(APIView):

    permission_classes = [
        IsAdmin,
    ]

    def patch(
        self,
        request,
        user_id,
    ):
        try:
            user = User.objects.get(
                id=user_id
            )
        except User.DoesNotExist:
            return Response(
                {
                    "detail": "User not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = UserRoleUpdateSerializer(
            user,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {
                "message": (
                    "User updated successfully."
                ),
                "user": UserSerializer(
                    user
                ).data,
            },
            status=status.HTTP_200_OK,
        )