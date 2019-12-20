"""concept URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import (HelloDjango, PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView, SignUp, UserProfile, EditProfile, ExploreView,
                    addLike, addComment, toggleFollow, FollowerInline)

urlpatterns = [
    path('', HelloDjango.as_view(), name="home"),
    path('posts', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/new/', PostCreateView.as_view(), name='create'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='edit'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('user_profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='profileedit'),
    path('explore', ExploreView.as_view(), name='explore'),
    path('follower/<int:pk>/', FollowerInline, name='follower'),
    path('like', addLike, name='addLike'),
    path('comment', addComment, name='addComment'),
    path('togglefollow', toggleFollow, name='togglefollow'),
    # path('post/profileedit/', ProfileEdit.as_view(), name='profileedit'),
]
