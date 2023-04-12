from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "password",
            "otp",
            "token_time_generated",
            "user_created_at",
            "token_used",
            "is_approved",
            "is_online",
            "is_active",
            "is_staff",
            "is_superuser",
            "is_verified",
            "is_suspended"
        ]


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            otp=validated_data['otp']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

