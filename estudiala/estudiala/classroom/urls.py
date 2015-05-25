from django.conf.urls import include, url
from . import views as views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^room/$', login_required(views.RoomView.as_view()), name="room"),
    url(r'^chat/$', login_required(views.ChatView.as_view()), name="chat")
]