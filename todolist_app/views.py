from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import Taskform
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":      #POST = get data from database
        form = Taskform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit = False)   #saves the form in database
            instance.manage = request.user
            instance.save()
        message = messages.success(request,('New Task Added!'))
        return redirect('todolist')
    else:
        all_task = TaskList.objects.filter(manage = request.user)   #this means hitting the default /todolist url here
        paginator = Paginator(all_task,10)         #paginator logic
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        return render(request, 'todolist.html', {"all_task" : all_task})
        #content will always be passed as form of dictionary
        # return HttpResponse('Hi Welcome to the task page')
  
def contact(request):
    context = {
        "contact_text" : "Welcome to Contact Page."
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        "about_text" : "Welcome to About Page."
    }
    return render(request, 'about.html', context)

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(TaskList, id=task_id)
    if task.manage == request.user:
        task.done = not task.done  # toggle status
        task.save()
    else:
        messages.error(request, 'You dont have the permission for this operation')
    return redirect('todolist')

@login_required
def delete_task(request, task_id):
   task = get_object_or_404(TaskList, id = task_id)
   if task.manage == request.user:
    task.delete()    #no need to save, save after delete is invalid
   else:
       messages.error(request, 'You do not have permission to delete this task.')
   return redirect('todolist') 


@login_required
def edit_task_name(request, task_id):
    task = get_object_or_404(TaskList, id=task_id)
    
    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todolist')
    else:
        form = Taskform(instance=task)
    
    return render(request, 'edit_task_name.html', {'form': form, 'task': task})


def index(request):
    context = {
        "index_text" : "Welcome to Taskmate."
    }
    return render(request, 'index.html', context)
    

    