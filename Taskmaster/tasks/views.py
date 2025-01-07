from django.shortcuts import render
from .models import Task

def index(request):
    tasks_todo = Task.objects.filter(completed=False).order_by('due_date')
    tasks_done = Task.objects.filter(completed=True).order_by('due_date')
    context = {
        'tasks_todo': tasks_todo,
        'tasks_done': tasks_done,
    }
    return render(request, 'tasks/index.html', context)