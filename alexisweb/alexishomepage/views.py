from django.http import Http404
from django.shortcuts import render
# from .models import Quote

def index(request):
    context = {}
    return render(request, 'alexishomepage/index.html', context)

def resume(request):
    context = {}
    return render(request, 'alexishomepage/resume.html', context)

def headshots(request):
    context = {}
    return render(request, 'alexishomepage/headshots.html', context)

def reel(request):
    context = {}
    return render(request, 'alexishomepage/reel.html', context)

def media(request):
    context = {}
    return render(request, 'alexishomepage/media.html', context)

def contact(request):
    context = {}
    return render(request, 'alexishomepage/contact.html', context)