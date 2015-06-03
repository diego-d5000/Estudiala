from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from . import forms as mForms
from .models import Chat, Room
from .serializers import ChatSerializer, RoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .utils import new_live_class

class RoomView(View):
        def get(self, req):
                if req.GET["n"] :
                        nroom = req.GET["n"]
                        roomid = Room.objects.get(n=nroom).id
                        user = req.user
                        return render(req, "classroom/room.html", locals())
                else:
                        return render(req, "classroom/error.html")

        def post(self, req):
                form = mForms.RoomForm(req.POST)
                if form.is_valid():
                        form.save()
                        new_live_class(req.POST)
                        return HttpResponse(status=status.HTTP_201_CREATED)
                else:
                        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

class ChatView(APIView):
        def get(self, req, format=None):
                if req.GET["id"] :
                        idchat = req.GET["id"]
                        chats = Chat.objects.filter(room__id=idchat)
                        serializer = ChatSerializer(chats, many=True)
                        return Response(serializer.data)

        def post(self, req, format=None):
                serializer = ChatSerializer(data=req.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomsApiView(APIView):
        def get(self, req, format=None):
                rooms = Room.objects.all()
                serializer = RoomSerializer(rooms, many=True)
                return Response(serializer.data)

def get_class_type(request, class_type):
    user = request.user
    #Crear instancia de roomtype
    all_classes = Room.objects.filter(r_type = class_type)
    return render(
        request,
        'classroom/class_type.html',
        {'all_classes': all_classes}
    )
