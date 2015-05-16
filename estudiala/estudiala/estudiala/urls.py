from classroom import urls as cl_urls
from django.conf.urls import include, url
from django.contrib import admin
from usuarios import views as usuarios_views
from tareas import views as tareas_views

urlpatterns = [
    url(r'^$', 'usuarios.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^classroom/$', include(cl_urls)),
    url(r'^cursos/kitchen/$','usuarios.views.kitchen_course', name='kitchen'),
    url(r'^cursos/math/$','usuarios.views.math_course', name='math'),
    url(r'^cursos/programming/$','usuarios.views.programming_course', name='programming'),
    url(r'^kitchen/$','usuarios.views.kitchen_course', name='kitchen'),
    url(r'^profile/$','usuarios.views.user_profile', name='profile'),
    url(r'^programming/$','usuarios.views.programming_course', name='programming'),
    url(r'^homework/success/$','tareas.views.homework_success',name='homework_success'),
    url(r'^homework/error/$','tareas.views.homework_error', name='homework_error'),

    #class-bassed-views
    url(r'^homework/$',tareas_views.homework.as_view(), name='homework'),
    url(r'^information/$', usuarios_views.information.as_view(), name='information'),
    url(r'^signin/$', usuarios_views.signin.as_view(), name='signin'),
    url(r'^signup/$', usuarios_views.signup.as_view(), name='signup'),

    #logout
    url(r'^close/$', 'usuarios.views.close', name='close'),]