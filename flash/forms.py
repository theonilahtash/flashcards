from django import forms
from .models import Profile,Card
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'post']

class NewCardForm(forms.ModelForm):
    class Meta:
        model = Card
        exclude = ['subject','title']

