from django import forms
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
# Create your models here.


class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(upload_to='static/images/posts',
                                format='JPEG', options={'quality': 100}, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])


class Member(AbstractUser):
    # first_name = forms.CharField(forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
    # last_name = forms.CharField(forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
    profile_pic = ProcessedImageField(upload_to='static/images/profiles',
                                      format='JPEG', options={'quality': 100}, blank=True, null=True)
