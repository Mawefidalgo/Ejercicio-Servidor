from django.urls import path
from . import views
from .views import TaskList, Details, NewForm
urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('details/<int:pk>/', Details.as_view(), name='detail'),
    path('new',NewForm.as_view(),name='new'),
]