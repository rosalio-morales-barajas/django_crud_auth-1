from django.urls import path
from django.contrib import admin
from django.http import HttpRequest
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_details, name='project_details'),
    path('tasks/', views.tasks, name='tasks'),
    path('new_task/', views.new_task, name='new_task'),
    path('new_project/', views.new_project, name='new_project'),
    path('project_details/', views.project_details, name='project_details') 
]
