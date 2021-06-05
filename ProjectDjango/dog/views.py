from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'dog/index.html', {
        'name': 'user',
        'age': '228',
        'list': ['1', '2', '3'],
        'dict': [
            {'main': {
                'name': 'igorek',
                'age': '322'
            }},
            {'main': {
                'name': 'aren',
                'age': '1488'
            }},
        ]
    })

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'dog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'dog/post_detail.html', {'post': post})

def turtle(request):
    return render(request, 'dog/turtle.html', {})

def work(request):
    return render(request, 'dog/work.html', {})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})

        
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
