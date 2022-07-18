from django import forms
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    ROLES = (
        ('Admin', 'Admin'),
        ('Team member', 'Team member'),
        ('Freelancer', 'Freelancer'),
    )
    role = forms.ChoiceField(required=True, choices=ROLES)

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2',"role",)