from django.shortcuts import render
from .forms import UserModelForm

# Create your views here.
def cadastro(request):
    form = UserModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'cadastro.html', {'form':form})