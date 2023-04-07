from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class BaseRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    # в классе мета, описана модель, по которой будет строиться форма и нужные поля
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
