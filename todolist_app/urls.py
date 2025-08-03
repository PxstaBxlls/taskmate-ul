# This file maps URLs within the 'todolist_app' to specific view functions
# These paths are relative to the '/task/' URL from the main project

from todolist_app import views
from django.urls import path
from todolist_app import views


urlpatterns = [
    path('', views.todolist,name = 'todolist'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('edit_task_name/<int:task_id>/',views.edit_task_name,name='edit_task_name'),
    path('delete/<int:task_id>/',views.delete_task, name = 'delete')
]
#as soon as it sees '' aka http://127.0.0.1:8000/task/
    #blank it calls views.todolist

#if it was path('abc', views.todolist,name = "todolist") i would have to do http://127.0.0.1:8000/task/abc
#to get the view.todolist response

#name = url name