from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def note(request):
    return render(request, 'note.html')


def send(request):
    return render(request, 'send.html')
