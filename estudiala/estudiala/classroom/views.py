from django.shortcuts import render

class Room:
	def get(self, req):
		if req.GET["n"] :
			num = req.GET["n"]
			user = req.user
			render(req, "classroom/room.html", locals())
		else:
			render(req, "classroom/error.html")
