from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Имя пользователя'}))
    password = forms.CharField(label='Пароль', required=False)
    email = forms.EmailField(required=True, error_messages='')
    class Meta:
        model = User
        fields = ('username','email', 'password')

