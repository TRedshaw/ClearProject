from django.shortcuts import render

def inhaler(request):
    # Renders the page 'inhaler.html' from the clear file in templates
    # Request is always the first bit
    return render(request, 'clear/inhaler.html')

def pollution(request):
    return render(request, 'clear/pollution.html')

def settings(request):
    return render(request, 'clear/settings.html')

# Create your views here.
