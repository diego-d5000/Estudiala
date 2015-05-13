from rest_framework import serializers
from django.forms import widgets
from models import Chat

class ChatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chat
		fields = ('username', 'role', 'text', 'date', 'room')
			
