from rest_framework import serializers
from .models import Message, User, Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["text", "sender", "reciver", "chat"]

class MessageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["text", "sender", "reciver", "chat", "createdAt", "id"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["userName", "password"]

class UserByUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["userName", "password", "id"]

    userName = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["name","user1", "user2", "id"]

    user1 = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user2 = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    id = serializers.IntegerField(allow_null = True)

class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["name", "user1", "user2"]

