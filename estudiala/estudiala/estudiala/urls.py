from classroom import urls as cl_urls
from usuarios import urls as us_urls
from tareas import urls as homework_urls
from django.conf.urls import include, url
from django.contrib import admin
from usuarios import views as usuarios_views

urlpatterns = [
    #home
    url('',include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', usuarios_views.home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^classroom/', include(cl_urls)),
    url(r'^usuarios/',include(us_urls)),
    url(r'^tareas/',include(homework_urls)),]