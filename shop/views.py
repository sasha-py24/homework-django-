from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html', {'title': 'About magazine'})


def page2(request):
    return render(request, 'page2.html', {'title': 'Page2'})


def page3(request):
    return render(request, 'page3.html', {'title': 'Page3'})










