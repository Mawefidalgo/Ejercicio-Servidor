from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views import View
from django.shortcuts import render, get_object_or_404

# Create your views here.

class TaskList(View):
    task = Task.objects.all()
    
    def actualizaTask(self):
        self.task = Task.objects.all()
        return self.task
    
    def get(self, request ):
        form= TaskForm()
        return render(request, 'todolist/task_list.html', {"tasks":self.actualizaTask(), "form":form} )
    
    def post(self, request):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'todolist/task_list.html', {"tasks":self.actualizaTask(), "form":form} )
    

class Details(View):
    def get(self, request, pk):
        details = get_object_or_404(Task, pk=pk)
        return render(request, 'todolist/detail.html', {'details': details})
    
class NewForm(View):
     def get(self, request ):
        form= TaskForm()
        return render(request, 'todolist/new.html', {"tasks":Task.objects.all(), "form":form} )