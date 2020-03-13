from django import forms

from .models import Post, Usuario

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha',)