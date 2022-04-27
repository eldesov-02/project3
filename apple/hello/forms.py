from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.forms import PasswordInput, EmailInput


class AddPostForm(forms.ModelForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-input', 'type': 'password'}))
    password2 = forms.CharField(label='Re-enter password',
                                widget=forms.PasswordInput(attrs={'class': 'form-input', 'type': 'password'}))
    first_name = forms.CharField(label='First_name',)
    last_name = forms.CharField(label='Last_name',)
    city = forms.CharField(label='Cities', widget=forms.TextInput(attrs={'class': 'form-input'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Postusers
        fields = ('username', 'password', 'password2', 'first_name', 'last_name', 'email', 'city', 'address')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Re-enter password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    city = forms.CharField(label='Cities', widget=forms.TextInput(attrs={'class': 'form-input'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'city', 'address')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


# class EmailPostForm(forms.Form):
#     email = forms.EmailField(label='name')
#     name = forms.CharField(max_length=25)
#     file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     comments = forms.CharField(max_length=100, widget=forms.Textarea)


class EmailForm(forms.Form):
    email = forms.EmailField(label='Пайдаланушы аты')
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)


