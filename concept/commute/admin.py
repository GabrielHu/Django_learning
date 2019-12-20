from django.contrib import admin
from .models import Post, Member, Like, Comment, UserConnection
# Register your models here.

admin.site.register(Post)
admin.site.register(Member)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserConnection)
