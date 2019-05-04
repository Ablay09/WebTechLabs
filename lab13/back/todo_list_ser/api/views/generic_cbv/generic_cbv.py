from rest_framework import generics

from api.models import TaskList, Task
from api.serializers import TaskSerializer, TaskListModelSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from django.http import Http404

class TaskListsAPIView(generics.ListCreateAPIView):
    serializer_class = TaskListModelSerializer
    permission_classes = (IsAdminUser, )
    queryset = TaskList.objects.all()



class TaskListTasksAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        try:
            taskList = TaskList.objects.get(id=self.kwargs['pk'])
        except TaskList.DoesNotExist:
            raise Http404

        queryset = taskList.tasks.all()
        return queryset

