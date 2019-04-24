from rest_framework import serializers
from api.models import Task, TaskList

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        tasklist = TaskList(**validated_data)
        tasklist.save()
        return tasklist

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=True)
    due_on = serializers.DateTimeField(required=True)
    status = serializers.CharField(required=True)
    task_list = TaskListSerializer(required=True)


    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.name = validated_data.get('created_at', instance.created_at)
        instance.name = validated_data.get('due_on', instance.due_on)
        instance.name = validated_data.get('status', instance.status)
        instance.name = validated_data.get('task_list', instance.task_list)
        instance.save()
        return instance

class Task2Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    status = serializers.CharField(required=True)