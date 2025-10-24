from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]