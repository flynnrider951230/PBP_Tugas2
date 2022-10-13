from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TaskForm
import datetime
from django.http import HttpResponse
from django.core import serializers

@login_required(login_url='/todolist/login/')
# Create your views here.
def show_todolist(request):
    data_task = Task.objects.all()
    context = {
    'list_task': data_task,
    'nama': 'Shafa',
    'last_login': request.COOKIES['last_login'],
}
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request): 
    context = {
    'nama': 'Shafa',
    'last_login': request.COOKIES['last_login'],
}
    return render(request, 'todolist_ajax.html', context)

def show_todolist_json(request):
    data_task = Task.objects.filter(user=request.user); 
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response 

def form (request):
    form = TaskForm()
    if (request.method == "POST"):
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False) 
            instance.user= request.user
            instance.date = datetime.datetime.now()
            instance.save()
            return redirect('todolist:show_todolist')
    context = {'form':form}
    return render(request, "taskbaru.html", context)

def add_task(request):
    if (request.method == 'POST'):
        title = request.POST.get('title')
        description = request.POST.get('description')

        new_task = Task.objects.create(
            title=title, 
            description=description, 
            date=datetime.datetime.now(),
            user=request.user, 
        )

        new_task.save()
        return HttpResponse("")
    return render(request, "taskbaru.html")