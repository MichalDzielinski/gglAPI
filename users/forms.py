from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your first name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your last name'}))
    username = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password','class': 'password'}))

    #reCAPTCHA token
    token = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class AuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=254, required=True, widget = forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(ModelForm):
    address = forms.CharField(max_length=100, required=True, widget= forms.MultipleHiddenInput())
    town = forms.CharField(max_length=100, required=True, widget= forms.MultipleHiddenInput())
    county = forms.CharField(max_length=100, required=True, widget= forms.MultipleHiddenInput())
    post_code = forms.CharField(max_length=8, required=True, widget= forms.MultipleHiddenInput())
    country = forms.CharField(max_length=40, required=True, widget= forms.MultipleHiddenInput())
    longitude = forms.CharField(max_length=50, required=True, widget= forms.MultipleHiddenInput())
    latitude = forms.CharField(max_length=50, required=True, widget= forms.MultipleHiddenInput())

    class Meta:
        model = UserProfile
        fields = ('address', 'town', 'county', 'post_code', 'country', 'longitude', 'latitude')
