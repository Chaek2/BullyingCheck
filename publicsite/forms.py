from django import forms
from django.forms import TextInput

class NameForm(forms.Form):
    app_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-controll','placeholder':'Название программы'}))