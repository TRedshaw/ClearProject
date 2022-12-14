from django.shortcuts import render
from django.http import HttpResponse


def inhaler(request):
    return HttpResponse('<h1>Inhaler Page</h1>')

def pollution(request):
    return HttpResponse('<h1>Pollution Page</h1>')

# Create your views here.
# hI CASSY