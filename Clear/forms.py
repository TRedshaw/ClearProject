from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm

from Clear.models import AppUser


class LoginForm(auth_forms.AuthenticationForm):
    class Meta(UserCreationForm):
        model = AppUser

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password','placeholder':'Password'}))


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AppUser
        fields = UserCreationForm.Meta.fields + ('dob', 'pollution_limit', 'consent')

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control ',
                  'id': 'username',
                  'placeholder': 'Username'}))

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                  'id': 'password1',
                  'placeholder': 'Password'}))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3',
                  'id': 'password2',
                  'placeholder': 'Password Confirmation'}))

    dob = forms.DateField(
        widget = forms.DateInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'onfocus':"(this.type='date')",
                   'placeholder': 'Date of Birth'}))

    pollution_limit = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'onfocus': "(this.type='number')",
                   'placeholder': 'Pollution Limit',
                   'min': 0,
                   'max': 10}))

    consent = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input',
                   'type': 'checkbox'}))

