from django.urls import path
from api import views

urlpatterns = [
    path('tasklists/', views.TaskListAPIView.as_view()),
    path('tasklists/<int:pk>/', views.TaskListDetailAPIView.as_view()),
    path('tasklist/<int:pk>/tasks/', views.TasksOfTaskListAPIView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailAPIView.as_view()),

    # path('tasklists/', views.task_list),
    # path('tasklists/<int:pk>/', views.task_list_detail),
    # path('tasklist/<int:pk>/tasks/', views.task_list_tasks),
    # path('tasks/<int:pk>/', views.task_detail),

    path('login', views.login),
    path('logout', views.logout),
    # path('tasklists/', views.TaskListsAPIView.as_view()),
    # path('tasklist/<int:pk>/tasks/', views.TaskListTasksAPIView.as_view()),
]