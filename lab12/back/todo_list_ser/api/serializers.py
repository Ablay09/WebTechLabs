from rest_framework import serializers
from api.models import Task, TaskList


class TaskListModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = TaskList
        fields = '__all__'

    def create(self, validated_data):
        taskList = TaskList(**validated_data)
        taskList.save()
        return taskList

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
    task_list = TaskListModelSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.due_on = validated_data.get('due_on', instance.due_on)
        instance.status = validated_data.get('status', instance.status)
        instance.task_list = validated_data.get('task_list', instance.task_list)
        instance.save()
        return instance
