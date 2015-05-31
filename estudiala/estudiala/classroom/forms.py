from django import forms
from .models import Room, Chat

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'n')

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('username', 'text', 'date', 'room')
    
