from django.urls import path
from . import consumers

wspatterns = [
    path('ws/chat/<int:id>/', consumers.PersonalChatConsumer.as_asgi())
]