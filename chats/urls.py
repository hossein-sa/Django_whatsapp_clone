from django.urls import path
from .views import ChatCreateView, ChatListView

urlpatterns = [
    path('create/', ChatCreateView.as_view(), name='create_chat'),
    path('list/', ChatListView.as_view(), name='list_chats'),
]
