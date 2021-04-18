from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class NewUserForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['email', 'username',
                  'password1', 'password2']

# class LoginForm(forms.ModelForm):
#     email = forms.EmailField()
#     password = forms.PasswordInput()

#     class Meta:
#         model = User
#         fields = ['email', 'passowrd']

class ProfileForm(forms.ModelForm):
    image = forms.ImageField()
    description = forms.TextInput()
    class Meta:
        model = Profile
        exclude = ('user',)

