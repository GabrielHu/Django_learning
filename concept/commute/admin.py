from django.contrib import admin
from .models import Post, Member, Like, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Member)
admin.site.register(Like)
admin.site.register(Comment)
