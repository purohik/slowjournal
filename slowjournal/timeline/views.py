from django.shortcuts import render, redirect
from .forms import forms

# Create your views here.
def index(request):
    form = forms.UsernameForm()
    return render(request, 'index.html', {'form': form})

def timeline(request):
    if request.method == 'POST':
        form = forms.UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            return render(request, 'timeline.html', {'username': username})
        else:
            return render(request, 'error.html')
    elif request.method == 'GET':
        # return redirect('index')
        form = forms.UsernameForm()
        return render(request, 'index.html', {'form': form})
                
def user(request):
    return render(request, 'user.html')

def user_timeline(request, username):
    return render(request, 'error.html', {'username': username})