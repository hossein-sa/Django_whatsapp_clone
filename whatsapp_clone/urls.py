from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # User API endpoints
    path('api/chats/', include('chats.urls')),  # Chat API endpoints
    path('api/messages/', include('chat_messages.urls')),  # Message API endpoints
]
