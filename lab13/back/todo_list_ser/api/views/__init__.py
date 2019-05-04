from .cbv.cbv import TaskListAPIView, TaskListDetailAPIView, TaskDetailAPIView, TasksOfTaskListAPIView
from .fbv.fbv import task_list, task_list_detail, task_list_tasks, task_detail
from .auth import login, logout
from .generic_cbv.generic_cbv import TaskListTasksAPIView, TaskListsAPIView