from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class reg_userSerializer(serializers.ModelSerializer):
    pass


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_date):
        user = User.objects.create_user(
            validated_date["username"], None, validated_date["password"]
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username")

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("unable to log in with provided credentials")




