import json


from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Group, Chat, UserProfile



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        print(f"WebSocket connected for room: {self.room_name}")

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        print(f"WebSocket disconnected for room: {self.room_name}, close_code: {close_code}")

    # Receive message from WebSocket
    @database_sync_to_async
    def save_chat_message(self, message, group, user_profile):
        chat = Chat(
            content=message,
            group=group,
            user=user_profile
        )
        chat.save()

    @database_sync_to_async
    def get_group(self):
        return Group.objects.get(name=self.room_name)

    @database_sync_to_async
    def get_or_create_user_profile(self):
        user = self.scope["user"]
        return UserProfile.objects.get_or_create(user=user)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        print(f"Received message from user {self.scope['user']} in group {self.room_group_name}: {message}")

        group = await self.get_group()
        user_profile, _ = await self.get_or_create_user_profile()


        await self.save_chat_message(message, group, user_profile)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

        print(f"Chat message saved to database and broadcasted to group: {self.room_group_name}")

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

        print(f"Sent message to WebSocket in group {self.room_group_name}: {message}")
