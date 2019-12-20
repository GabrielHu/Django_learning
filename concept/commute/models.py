from django import forms
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
# Create your models here.


class Member(AbstractUser):
    profile_pic = ProcessedImageField(upload_to='static/images/profiles',
                                      format='JPEG', options={'quality': 100}, blank=True, null=True)

    def get_connections(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()


class Post(models.Model):
    author = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='my_posts')
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(upload_to='static/images/posts',
                                format='JPEG', options={'quality': 100}, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

    def get_like_count(self):
        return self.likes.count()

    def get_comment_count(self):
        return self.comments.count()


class Like(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='likes')
    user = models.ForeignKey(Member,
                             on_delete=models.CASCADE,
                             related_name='likes')

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' likes ' + self.post.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=1000)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment


class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="friendship_creator_set"
    )
    following = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="friend_set"
    )

    def __str__(self):
        return self.creator.first_name + ' follows ' + self.following.first_name
