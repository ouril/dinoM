from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):                                                                
    class Meta:
        model = User
        fields = ('username','email')

class UserChangeForm(forms.ModelForm):
    """
    Форма для обновления данных пользователей. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя.
    """

    class Meta:
        model = User
        fields = ('username', 'email')