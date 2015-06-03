from rest_framework import serializers
from django.forms import widgets
from .models import Chat, Room

class ChatSerializer(serializers.ModelSerializer):
        class Meta:
                model = Chat
                fields = ('username', 'role', 'text', 'date', 'room')

class RoomSerializer(serializers.ModelSerializer):
        class Meta:
                model = Room
                fields = ('name', 'n', 't_type')
