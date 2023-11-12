from django import forms

class UsernameForm(forms.Form):
    username = forms.CharField(label = 'Enter your username', max_length=64)