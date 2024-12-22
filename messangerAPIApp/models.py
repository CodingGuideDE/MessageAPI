from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=1000)
    sender = models.ForeignKey("User" ,related_name="CreationUser" ,on_delete=models.CASCADE)
    reciver = models.ForeignKey("User" ,related_name="ReciverUser" , on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=True)
    chat = models.ForeignKey("Chat", on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now=True)

class Chat(models.Model):
    name = models.CharField(max_length=200, null=True)
    user1 = models.ForeignKey(User, related_name="user1", on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name="user2", on_delete=models.CASCADE)
