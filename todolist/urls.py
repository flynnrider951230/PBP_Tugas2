from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import form
from todolist.views import show_todolist_json
from todolist.views import show_todolist_ajax
from todolist.views import add_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', form, name='create-task'),
    path('json/', show_todolist_json, name='json'),
    path('todolist_ajax/', show_todolist_ajax, name='ajax'),
    path('add_task/', add_task, name='add_task'),
]