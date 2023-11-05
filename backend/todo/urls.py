from django.urls import path
from .views import TaskList, TaskCreate, TaskDestroy, TaskEdit

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/create/', TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>/delete/', TaskDestroy.as_view(), name='task-destroy'),
    path('tasks/<int:pk>/edit/', TaskEdit.as_view(), name='task-edit'),
]
