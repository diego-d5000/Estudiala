from django.conf.urls import url
from usuarios import views as usuarios_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #url(r'^kitchen/$',usuarios_views.kitchen_course.as_view(), name='kitchen'),
    #url(r'^math/$',usuarios_views.math_course.as_view(), name='math'),
    #url(r'^programming/$',usuarios_views.programming_course.as_view(), name='programming'),
    url(r'^nouser/$',usuarios_views.no_user.as_view(), name='nouser'),
    url(r'^signin/$', usuarios_views.signin.as_view(), name='signin'),
    url(r'^signup/$', usuarios_views.signup.as_view(), name='signup'),
    #login_required
    url(r'^information/$', login_required(usuarios_views.information.as_view()), name='information'),
    url(r'^profile/$',login_required(usuarios_views.user_profile.as_view()), name='profile'),
    url(r'^close/$','usuarios.views.close', name='close'),]
