from api.models import Task, TaskList
from api.serializers import TaskListModelSerializer, TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class TaskListAPIView(APIView):
    #Get all task lists
    def get(self, request):
        taskLists = TaskList.objects.all()
        serializer = TaskListModelSerializer(taskLists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Create task list
    def post(self, request):
        serializer = TaskListModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #Delete all task list
    def delete(self, request):
        taskLists = TaskList.objects.all()
        taskLists.delete()
        return Response("Deleted all Task Lists", status=status.HTTP_204_NO_CONTENT)


class TaskListDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        taskList = self.get_object(pk)
        serializer = TaskListModelSerializer(taskList)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        taskList = self.get_object(pk)
        serializer = TaskListModelSerializer(instance=taskList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        taskList = self.get_object(pk)
        taskList.delete()
        return Response("Task list successfully deleted", status=status.HTTP_204_NO_CONTENT)

class TaskDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response("Task successfully deleted", status=status.HTTP_204_NO_CONTENT)

class TasksOfTaskListAPIView(APIView):
    def get_task_list(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        taskList = self.get_task_list(pk)
        tasksOfTaskList = taskList.tasks.all()
        serializer = TaskSerializer(tasksOfTaskList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        taskList = self.get_task_list(pk)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task_list=taskList)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
