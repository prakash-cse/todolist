from django import forms
from django.forms import ModelForm
from .models import *

class todoform(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = activity
        fields = '__all__'
