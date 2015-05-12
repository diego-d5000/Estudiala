from django.shortcuts import render
from django.views.generic import TemplateView

class Room(TemplateView):
	def get(self, req):
		if req.GET["n"] :
			num = req.GET["n"]
			user = req.user
			render(req, "classroom/room.html", locals())
		else:
			render(req, "classroom/error.html")
