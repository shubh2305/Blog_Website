from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput())
    last_name = forms.CharField(max_length=20)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'password1', 'password2']
