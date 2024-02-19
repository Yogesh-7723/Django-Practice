from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    task = Task.objects.all()
    return render(request,"index.html",{'task':task})  



def addtask(request):
    if request.method == 'POST':
        task_name = request.POST['task_name']
        due_date = request.POST['due_date']
        if True:
            Task.objects.create(task_name=task_name,
                            due_date=due_date)
            return redirect('/')

def delete(request,uid):
    Task.objects.get(id=uid).delete()
    return redirect('/')


def success(request,qk):
        status = Task.objects.get(id=qk)
        if status.completed == True :
            status.completed = False
        else:
            status.completed = True
        status.save()
        return redirect("/")