from django.urls import path
from . import views

#define the urls
urlpatters = [
    path('tasks/', views.tasks),
    path('tasks/<int:pk>/', views.task_detail),
]