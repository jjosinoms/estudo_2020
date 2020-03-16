from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name':forms.TextInput,
            'last_name':forms.TextInput,
            'email':forms.TextInput,
            'password':forms.TextInput,
            'username':forms.TextInput,
        }
        '''error_message ={
            'first_name': {'required' : 'Este Campo e Obrigatorio!'}
        }'''