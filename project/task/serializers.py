from rest_framework import serializers

from app.models import UserProfile
from .models import TaskModel


class CreateTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"



