from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
# Create your views here.

def homepage(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, "main/home.html", {
        "todo_items": todo_items,
    })

def add(request):
    current_date = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
