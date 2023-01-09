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

class SettingsForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'username', 'placeholder': 'Username'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'surname', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'surname', 'placeholder': 'Surname'}))
    home_postcode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'home_postcode', 'placeholder': 'home Postcode'}))
    work_postcode = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'work_postcode', 'placeholder': 'Work Postcode'}))
    other_postcode = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'other_postcord', 'placeholder': 'Other Postcode'}))

    class Meta:
        model = AppUser
        fields=['username','first_name','last_name','home_postcode','work_postcode','other_postcode']


# # TODO FIX
# class CurrentLocationForm(forms.ModelForm):
#     current_location = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'current_location', 'placeholder': 'Current Location'}))
#
