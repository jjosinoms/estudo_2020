from django.shortcuts import render
from .models import Post, Usuario
from django.utils import timezone
from .forms import PostForm, UsuarioForm
# Create your views here.
def verificaLogin(request):
    print("ola meu camarada")
    buscas = Usuario.objects.all()

    return render(request, 'home.html', {'buscas':buscas})

def cadastro_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.email = request.user
            usuario.save()
    else:
        form = UsuarioForm()
    return render(request, 'cadastroUsuario.html',{'form':form})

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