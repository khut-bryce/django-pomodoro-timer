# Allows creation of functions for routes
# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World")
    # the render function literally renders our html pages
    return render(request, 'home.html')

def settings(request):
    # return HttpResponse("Settings page")
    return render(request, 'settings.html')
