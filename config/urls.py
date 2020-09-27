"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from main import views
from . import settings

urlpatterns = [
    path('api/v1/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('admin/', admin.site.urls)]

# catch all other URL
urlpatterns += [re_path(r'^.*/$', views.top, name='indexView')]
urlpatterns += [path('', views.terms_of_service, name='indexView')]