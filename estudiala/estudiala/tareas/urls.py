from django.conf.urls import url
from tareas import views as tareas_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^homework/success/$',login_required(tareas_views.homework_success.as_view()),name='homework_success'),
    url(r'^homework/error/$',login_required(tareas_views.homework_error.as_view()), name='homework_error'),
    url(r'^homework/$',login_required(tareas_views.homework.as_view()), name='homework'),
    url(r'^consulta/$',tareas_views.get_homework, name="get_homework")]