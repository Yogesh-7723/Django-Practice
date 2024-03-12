from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Student
from django.contrib import messages
# Create your views here.

def index(request):
    student = Student.objects.all()
    return render(request,'crm/index.html',{'student':student})

def demo(request):
    data = Student.objects.all()
    return render(request,"crm/demo.html",{'data':data})

def base(request):
    return render(request,'crm/base.html')

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully open home page')
            return redirect('/crm1/')
        else:
            messages.error(request,"User name or Password wrong !")
            return render(request,'crm/home.html')
    else: 
        return render(request,'crm/home.html')
    
def student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contect = request.POST['contect']
        course = request.POST['course']
        branch = request.POST['branch']
        year_sem = request.POST['year_sem']
        cgpa = request.POST['cgpa']
        result = request.FILES.get('result')
        if name is None or email is None or contect is None or course is None or branch is None or year_sem is None or cgpa is None or result is None:
            messages.error(request,"Invalid detaild of student !")
            return render(request,'crm/student.html')
        
        else:
            Student.objects.create(name=name,email=email,contect=contect,course=course,branch=
            branch,year_sem=year_sem,cgpa=cgpa,result=result)
            messages.success(request,"Student Add Successfully !")
            return redirect('/crm1/student/')
    else:
        return render(request,'crm/student.html')