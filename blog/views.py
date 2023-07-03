from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, User

class PostView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'

class PostDetail(DetailView): 
    model = Post
    template_name = 'post_detail.html'
    
class PostCreate(CreateView): 
    model = Post
    template_name = 'post_new.html'
    fields = ['name', 'author', 'body']

class PostUpdate(UpdateView): 
    model = Post
    template_name = 'post_edit.html'
    fields = ['name', 'body']

class PostDelete(DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class UserView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'user_list'

class UserCreate(CreateView): 
    model = User
    template_name = 'user_new.html'
    fields = ['first_name','last_name','phone','email','skills']

class UserDetail(DetailView): 
    model = User
    template_name = 'user_detail.html'
    

class UserUpdate(UpdateView): 
    model = User
    template_name = 'user_edit.html'
    fields = ['first_name','last_name','phone','email','skills']

class UserDelete(DeleteView): 
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('users')