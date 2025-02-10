from django.urls import path
from .views import MessageCreateView, MessageListView

urlpatterns = [
    path('create/', MessageCreateView.as_view(), name='create_message'),
    path('chat/<uuid:chat_id>/', MessageListView.as_view(), name='list_messages_by_chat'),
]
