from django.contrib import admin
from .models import UserProfileModel, ChatModel


# Register your models here.
admin.site.register(ChatModel)
admin.site.register(UserProfileModel)
