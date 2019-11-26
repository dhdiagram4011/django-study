from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = reg_user
        fields = ("email")

    def create(self, validated_date):
        user = reg_user.objects.create_user(
            validated_date["email"], None, validated_date["email"]
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = reg_user
        fields = ("email")

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("unable to log in with provided credentials")




