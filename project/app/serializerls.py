from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from app.models import CustomUser, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only': True}}
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

    def save(self,**kwargs):
        user = self.validated_data["user"]
        obj = CustomUser.objects.get(id=user.id)
        self.validated_data["email"] = obj.email
        self.validated_data["phone_number"] = obj.phone_number

        super(UserProfileSerializer, self).save(**kwargs)
