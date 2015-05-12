from django.conf.urls import include, url
from . import views as views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^room/$', login_required(views.Room.as_view()), name="room")
]