from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfileModel, NotificationModel
import json

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=NotificationModel)
def send_notification(sender, instance, created, **kwargs):
    print ("Inside Notification Signal before")
    if created:
        print("Inside Notification Signal")
        channel_layer = get_channel_layer()
        notification_obj = NotificationModel.objects.filter(is_seen=False, user=instance.user).count()
        user_id = str(instance.user.id)
        user_group_name = f"notification_{instance.user.id}"
        data = {
            'count':notification_obj
        }

        async_to_sync(channel_layer.group_send)(
            user_group_name, {
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )


@receiver(post_save, sender=UserProfileModel)
def send_onlineStatus(sender, instance, created, **kwargs):
    if not created:
        channel_layer = get_channel_layer()
        user = instance.user.username
        user_status = instance.online_status

        data = {
            'username':user,
            'status':user_status
        }
        async_to_sync(channel_layer.group_send)(
            'user', {
                'type':'send_onlineStatus',
                'value':json.dumps(data)
            }
        )