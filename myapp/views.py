from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks
from .forms import createNewTask, createNewProject

# Create your views here.


def index(request):
    titulo = 'Bienvenidos al curso de Django!!!...'
    return render(request, 'index.html', {
        'title': titulo
    })


def about(request):
    usuario = "Rosalio Morales Barajas"
    return render(request, 'about.html', {
        'desarrollador': usuario
    })


def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = Tasks.objects.get(id=id)
    # task = get_object_or_404(Tasks, id=id)
    tarea = list(Tasks.objects.all())
    return render(request, 'tasks.html', {
        'tareas': tarea
    })


def new_task(request):
    # print(request.GET['title'])
    # print(request.GET['description'])
    if request.method == 'GET':
        return render(request, 'create_new_task.html', {
            'form': createNewTask()
        })
    else:
        Tasks.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=3)
        return redirect(tasks)


def new_project(request):
    if request.method == 'GET':
        return render(request, 'create_new_project.html', {
            'form': createNewProject
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect(projects)
    
def project_details(request, id):
    projects = get_object_or_404(Project, id=id)
    tasks = Tasks.objects.filter(project_id=id)
    return render(request, 'project_details.html', {
        'projects': projects,
        'tasks': tasks
    })  
    

          
