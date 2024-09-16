from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from usersApp.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Пароль не совпадает!"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"]
        )

        user.set_password(validated_data["password1"])
        user.save()

        return user
