from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%m/%d/%Y, %I:%M %p",  read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
