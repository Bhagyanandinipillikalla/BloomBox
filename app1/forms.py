from django import forms
from .models import Plant
from django.contrib.auth.models import User

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"


class AccountForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']


class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,label="Username")
    password=forms.CharField(widget=forms.PasswordInput)        

