from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from . models import Task

# Create your views here.

def home(request):
    if request.method == 'POST':
        task_text = request.POST['task']
        if task_text:
            task = Task.objects.create(task=task_text)
            task.save()
        else:
            return HttpResponseRedirect(request.path)
    tasks_not_completed = Task.objects.filter(is_completed=False)
    tasks_completed = Task.objects.filter(is_completed=True)
    context = {'tasks_not_completed':tasks_not_completed,
               'tasks_completed':tasks_completed,}
    return render(request, 'home.html', context)

def edit_task(request, id):
    get_task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        task_text = request.POST['task']
        if task_text:
            get_task.task=task_text
            get_task.save()
            return redirect('home')
        else:
            return HttpResponseRedirect(request.path)
    
    context = {'get_task':get_task,}
    return render(request, 'edit_task.html', context)

def status_change(request, id):
    task = get_object_or_404(Task, pk=id)
    if task.is_completed == True:
        task.is_completed = False
        task.save()
    else:
        task.is_completed = True
        task.save()
    return redirect('home')


def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('home')