from django.urls import path
from api import views

urlpatterns = [
    path('tasklists/', views.tasklist_list),
    path('tasklists/<int:pk>/', views.tasklist_detail),
    path('tasklist/<int:pk>/tasks/', views.tasklist_task),

    path('tasks/', views.task_list),
    path('tasks/<int:pk>/', views.task_detail)
]