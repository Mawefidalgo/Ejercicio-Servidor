from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views import View
# Create your views here.

class TaskList(View):
    task = Task.objects.all()

    def actuslizaTask(self):
        self.task = Task.objects.all()
        return self.task
    
    def get(self, request):
        form= TaskForm()
        return render(request, 'todolist/task_list.html', {"task":self.actuslizaTask(), "form":form} )
    
    def post(self, request):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'todolist/task_list.html', {"task":self.actuslizaTask(), "form":form} )
    

