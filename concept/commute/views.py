from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Member, Like, Comment

from .forms import MemberCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from annoying.decorators import ajax_request
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


class UserProfile(LoginRequiredMixin, DetailView):
    model = Member
    template_name = 'profile.html'
    login_url = 'login'


class EditProfile(LoginRequiredMixin, UpdateView):
    model = Member
    template_name = 'profileedit.html'
    fields = ['profile_pic', 'username']
    login_url = 'login'


@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }


@ajax_request
def addComment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    commenter_info = {}

    try:
        comment = Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        username = request.user.username

        commenter_info = {
            'username': username,
            'comment_text': comment_text
        }

        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'post_pk': post_pk,
        'commenter_info': commenter_info
    }
