from classroom import urls as cl_urls
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'usuarios.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^classroom/', include(cl_urls)),
    url(r'^close/$', 'usuarios.views.close', name='close'),
    url(r'^cursos/kitchen/$','usuarios.views.kitchen_course', name='kitchen'),
    url(r'^cursos/math/$','usuarios.views.math_course', name='math'),
    url(r'^cursos/programming/$','usuarios.views.programming_course', name='programming'),
    url(r'^homework/$','tareas.views.homework', name='homework'),
    url(r'^information/$','usuarios.views.information', name='information'),
    url(r'^kitchen/$','usuarios.views.kitchen_course', name='kitchen'),
    url(r'^profile/$','usuarios.views.user_profile', name='profile'),
    url(r'^programming/$','usuarios.views.programming_course', name='programming'),
    url(r'^signin/$', 'usuarios.views.signin', name='signin'),
    url(r'^signup/$', 'usuarios.views.signup', name='signup'),
    url(r'^homework/success/$','tareas.views.homework_success',name='homework_success'),
    url(r'^homework/error/$','tareas.views.homework_error', name='homework_error'),]
