from rest_framework import serializers
from api.models import Task, TaskList
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ("id", "username", "email")


class TaskListModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    owner = UserSerializer(read_only=True)

    def create(self, validated_data):
        taskList = TaskList(**validated_data)
        taskList.save()
        return taskList

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=False)
    due_on = serializers.DateTimeField(required=True)
    status = serializers.CharField(required=True)
    owner = UserSerializer(read_only=True)
    task_list = TaskListModelSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.due_on = validated_data.get('due_on', instance.due_on)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance