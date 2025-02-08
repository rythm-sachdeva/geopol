from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json
from channels.db import database_sync_to_async
from .models import ChatModel,UserProfileModel, NotificationModel
from django.contrib.auth import get_user_model
from .serializers import ChatSerializer

User = get_user_model()


class PersonalChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        request_user = self.scope['user']
        if request_user.is_authenticated:
            chat_with_user = self.scope['url_route']['kwargs']['id']
            user_ids = [int(request_user.id), int(chat_with_user)]
            user_ids = sorted(user_ids)
            self.room_group_name = f'personal_chat_{user_ids[0]}-{user_ids[1]}'
            # print(self.room_group_name)
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
                )
        await self.accept()
    
    async def receive(self,text_data=None,bytes_data=None):
        # print("Inside Recieve Functions")
        data = json.loads(text_data)
        print(data)
        username = data['email']
        reciever = self.scope['url_route']['kwargs']['id']
        message = data['message']
        messageObj = await self.save_message(self.scope['user'], self.room_group_name, message, reciever)
        serialiser = ChatSerializer(messageObj)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':serialiser.data,
                'username':username,
            }
        )

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def chat_message(self,event):
        message = event['message']
        encodedmessage = json.dumps(message)

        await self.send(text_data=encodedmessage)
    
    @database_sync_to_async
    def save_message(self, user, thread_name, message, receiver):
        receiver_User = User.objects.get(id=receiver)
        chat_obj = ChatModel.objects.create(
            sender=user, message=message, thread_name=thread_name,reciever=receiver_User)
        other_user_id = self.scope['url_route']['kwargs']['id']
        get_user = User.objects.get(id=other_user_id)
        if receiver == get_user.email:
            NotificationModel.objects.create(chat=chat_obj, user=get_user)
        return chat_obj


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        my_id = self.scope['user'].id
        self.room_group_name = f'notification_{my_id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    
    async def disconnect(self, code):
        return await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    


    async def send_notification(self, event):
        data = json.loads(event.get('value'))
        count = data['count']
        print(count)
        await self.send(text_data=json.dumps({
            'count':count
        }))

class OnlineStatusConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'user'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, code):
        return await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = json.loads(text_data)
        username = data['email']
        connection_type = data['type']
        print(connection_type)
        await self.change_online_status(username, connection_type)
    
    async def send_onlineStatus(self, event):
        data = json.loads(event.get('value'))
        username = data['email']
        online_status = data['status']
        await self.send(text_data=json.dumps({
            'username':username,
            'online_status':online_status
        }))

    
    @database_sync_to_async
    def change_online_status(self, email, c_type):
        user = User.objects.get(email=email)
        userprofile = UserProfileModel.objects.get(user=user)
        if c_type == 'open':
            userprofile.online_status = True
            userprofile.save()
        else:
            userprofile.online_status = False
            userprofile.save()
        



   