from rest_framework import serializers
from .models import CustomUser, UserProfile
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def save(self, **kwargs):
        self.validated_data["password"] = make_password(self.validated_data["password"])
        self.validated_data["is_active"] = True
        super(UserSerializer, self).save(**kwargs)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("phone_number", "password")


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
