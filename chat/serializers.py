from time import strftime
from rest_framework.serializers import ModelSerializer
from .models import Chat
from rest_framework import serializers


class ChatSerializer(ModelSerializer):

    url = serializers.SerializerMethodField()
    timestamp = serializers.DateTimeField(format="%b. %d, %Y, %I:%M %p")

    def get_url(self , obj):
        return obj.user.get_absoloute_url()


    class Meta:
        model = Chat
        fields = ("text" , "user" , "timestamp" , "url")

        depth = 1
    