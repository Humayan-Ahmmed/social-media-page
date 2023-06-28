from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CreateNewUser(UserCreationForm):

    Email=forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'username'}))
    password1=forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2=forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'confirm password'}))



    class Meta:
        model=User
        fields=('Email','username','password1','password2')

class Edit_ProfileForm(forms.ModelForm):
    dob=forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile
        exclude = ('user',)
