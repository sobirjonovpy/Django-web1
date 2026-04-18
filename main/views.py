from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class Home(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-id']
    

class More(DetailView):
    model = Post
    template_name = 'more.html'
    context_object_name = 'post'


class Create(CreateView):
    model = Post
    fields = ['title', 'desc', 'img', 'url']
    template_name = 'create.html'
    success_url = reverse_lazy('home')  


class Edit(UpdateView):
    model = Post
    fields = ['title', 'desc', 'img', 'url']
    template_name = 'create.html'
    success_url = '/'


class Delete(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'delete.html'