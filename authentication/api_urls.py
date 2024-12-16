from django.urls import path

from .views import UserRegisteration, LoginView
from knox.views import LogoutAllView, LogoutView

urlpatterns = [
    path('api/auth/register/', UserRegisteration.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/auth/logoutall/', LogoutAllView.as_view(), name='logoutall'),
]
