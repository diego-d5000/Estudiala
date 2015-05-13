from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from . import forms as mForms
from models import Chat, Room
from serializers import ChatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class RoomView(TemplateView):
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
			url = "/classroom/room?n="
			url + req.POST["n"]
			return redirect(url)

class ChatView(APIView):
	def get(self, req, format=None):
	 	if req.GET["n"] :
			nroom = req.GET["n"]
			chats = Chat.objects.filter(room__n=nroom)
			serializer = ChatSerializer(chats, many=True)
			return Response(serializer.data)


	def post(self, req, format=None):
		print (req.POST)
		serializer = ChatSerializer(data=req.data)
		if serializer.is_valid():
	  		serializer.save()
	  		return Response(serializer.data, status=status.HTTP_201_CREATED)
	  	else:
	  		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



