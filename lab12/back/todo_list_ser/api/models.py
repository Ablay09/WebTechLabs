from django.db import models
import datetime


now = datetime.datetime.now()


class TaskList(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    # class Meta:
    #     verbose_name = 'TaskList'
    #     verbose_name_plural = 'TaskLists'

class Task(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=now)
    due_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=100)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)
