from django.db import models
from django.conf import settings

# Create your models here.

class UserProfileModel(models.Model):
   user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   name = models.CharField(max_length=100, null=True, blank=True)
   online_status = models.BooleanField(default=False)

   def __str__(self)->str:
         return self.name




class ChatModel(models.Model):
    sender = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    message = models.TextField(null=True, blank=True)
    reciever = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reciever')
    thread_name= models.CharField(max_length=100, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message
    
class NotificationModel(models.Model):
    chat = models.ForeignKey(to=ChatModel, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)


    def __str__(self):
        return self.user.email 
    

