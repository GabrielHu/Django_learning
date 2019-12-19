from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

from .forms import MemberCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HelloDjango(TemplateView):
    template_name = 'home.html'  # this is a parameter of TemplateView


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "index.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "create.html"
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    template_name = "edit.html"
    fields = '__all__'


class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy('posts')


class SignUp(CreateView):
    form_class = MemberCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
