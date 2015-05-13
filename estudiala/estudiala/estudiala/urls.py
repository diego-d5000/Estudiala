"""estudiala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from classroom import urls as cl_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'usuarios.views.home', name='home'),
    url(r'^math/$','usuarios.views.math_course', name='math'),
    url(r'^programming/$','usuarios.views.programming_course', name='programming'),
    url(r'^kitchen/$','usuarios.views.kitchen_course', name='kitchen'),
    url(r'^profile/$','usuarios.views.user_profile', name='profile'),
    url(r'^signup/$', 'usuarios.views.signup', name='signup'),
    url(r'^signin/$', 'usuarios.views.signin', name='signin'),
    url(r'^close/$', 'usuarios.views.close', name='close'),
    url(r'^information/$','usuarios.views.information', name='information'),
    url(r'^homework/$','tareas.views.homework', name='homework'),
    url(r'^classroom/$', include(cl_urls)),
]
