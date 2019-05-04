from django.db import models
import datetime
from django.contrib.auth.models import User

now = datetime.datetime.now()



class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class TaskList(models.Model):
    name = models.CharField(max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    objects = TaskListManager()


    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'

class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class Task(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    due_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=100)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    objects = TaskManager()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)
