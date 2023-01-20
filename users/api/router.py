from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.api.views import RegisterView, UserView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('user', UserView.as_view())
]