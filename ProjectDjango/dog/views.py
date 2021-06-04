from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

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
