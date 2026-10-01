from rest_framework import serializers

from .models import Department


class DepartmentSerializer(
    serializers.ModelSerializer
):

    user_count = serializers.IntegerField(
        source="users.count",
        read_only=True,
    )

    class Meta:
        model = Department

        fields = [
            "id",
            "name",
            "code",
            "description",
            "is_active",
            "user_count",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user_count",
            "created_at",
            "updated_at",
        ]