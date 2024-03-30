from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NameForm


def home(request):
    return render(request, 'publicsite/home.html')


def search(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            data = {
                'error': form.cleaned_data['app_name'],
                'forms': form,
                'apps': {
                    '1': {
                        'url': 'asfs',
                        'email': 'gtg'
                    },
                    '2': {
                        'url': 'tht',
                        'email': 'plk'
                    }
                }
            }
            return render(request, 'publicsite/search.html', data)
    else:
        form = NameForm()
        data = {
            'forms': form
        }
        return render(request, 'publicsite/search.html', data)
