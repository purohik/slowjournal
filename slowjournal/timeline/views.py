from django.shortcuts import render
from .forms import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def timeline(request):
    if request.method == 'POST':
        form = forms.UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print('\n\n\n\n', username, '!!\n\n')
            return render(request, 'timeline.html', {'username': username})
        else:
            return render(request, 'error.html')
    else:
        form = forms.UsernameForm()
        return render(request, 'index.html', {'form': form})

def user(request):
    return render(request, 'user.html')