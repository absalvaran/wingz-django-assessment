from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "role",
            "first_name",
            "last_name",
            "phone_number",
        )


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "role",
            "first_name",
            "last_name",
            "phone_number",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                email=email,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
