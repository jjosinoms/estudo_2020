from django.shortcuts import render
from .models import Post 
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()
    return render(request, 'novo_post.html', {'form': form})

def home(request):
    nome = 'Jonas'
    sobrenome = 'Monteiro'
    posts = Post.objects.all()
    return render(request, 'home.html', {'nome': nome, 'sobrenome':sobrenome, 'posts':posts})