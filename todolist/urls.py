from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.task_list, name='task_list'),
]