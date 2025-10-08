"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# This is for when I want to include my other apps
# from django.urls import path, include

from . import views

# ARGUEMENTS FOR "path": 
# 1. The URL pattern string — e.g., '', 'settings/', 'about/'
# This is the part of the URL that comes after your domain.
# '' means the root URL (http://127.0.0.1:8000/)
# 'settings/' means http://127.0.0.1:8000/settings/

# 2. The view function to call — e.g., views.homepage, views.settings
# This is the Python function in views.py that handles the request and returns a response.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('settings/', views.settings),
    #path('todo_app/', include('todo_app.urls'))
]
