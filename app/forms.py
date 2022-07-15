from dataclasses import field
from importlib.resources import contents
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class RestoranForm(forms.ModelForm):
    class Meta:
        model = Restoran
        fields = '__all__'


class CreateFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = '__all__'


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': '4',}))

    class Meta:
        model = Comment
        fields = ('content',)