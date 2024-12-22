from django.contrib import admin
from django.urls import path
from messangerAPIApp.views import MessagesListView, UserListView, UserCreateAPIView, ChatByUserView,MessageCreateAPIView, ChatCreateAPIView, ChatListView, UserDetailView, ChatMessageView, UserByUsernameView, ChatDeleteView, MessageDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', MessagesListView.as_view(), name='messages'),
    path('users/', UserListView.as_view(), name='users'),
    path('users/add/', UserCreateAPIView.as_view(), name='createUser'),
    path('messages/add/', MessageCreateAPIView.as_view(), name='createMessage'),
    path('chats/add/', ChatCreateAPIView.as_view(), name='chat-add'),
    path('chats/', ChatListView.as_view(), name='chatsList'),
    path('users/<int:id>/', UserDetailView.as_view(), name='userDetailView'),
    path('messages/chat/', ChatMessageView.as_view(), name='chatGet'),
    path('users/<str:userName>/', UserByUsernameView.as_view(), name='userNameView'),
    path('chats/delete/<int:pk>/', ChatDeleteView.as_view(), name='chatDelete'),
    path('messages/delete/<int:pk>', MessageDeleteView.as_view(), name='deleteMessage'),
    path('chats/user/', ChatByUserView.as_view(), name='chatUserView'),
    
]
