from django.urls import path
from .auth_views import RegisterView, LoginView, RefreshTokenView
from .views import UserListView

urlpatterns = [
    path('list/', UserListView.as_view(), name='user-list'),
    path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token-refresh'),
]
