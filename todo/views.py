from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.all().order_by('-created_at')

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title:
            Task.objects.create(title=title, description=description)
        return redirect("index")

    return render(request, "index.html", {"tasks": tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("index")

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.save()
        return redirect("index")
    return render(request, "edit.html", {"task": task})
