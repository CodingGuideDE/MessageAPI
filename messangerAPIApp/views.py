from rest_framework import generics
from .models import Message, User, Chat
from django.shortcuts import render
from .serializer import MessageSerializer, UserSerializer, ChatSerializer, UserByUsernameSerializer, ChatCreateSerializer, MessageGetSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q



class ChatCreateAPIView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatCreateSerializer

class ChatListView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MessagesListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserByUsernameView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserByUsernameSerializer
    lookup_field = 'userName'

class MessageCreateAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ChatDeleteView(generics.DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MessageDeleteView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageGetSerializer

class ChatByUserView(generics.ListAPIView):
    serializer_class = ChatSerializer
    
    def get_queryset(self):
        user = self.request.query_params.get('user1', None)
        if not user:
            return Chat.objects.none()  # Leeres Queryset, wenn kein `user_id` angegeben wird.
            
        return Chat.objects.filter(Q(user1_id=user) | Q(user2_id=user))

class ChatMessageView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageGetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender', 'reciver', 'chat']
