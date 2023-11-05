from django.urls import path
from users.views import UserCreateView, UserLoginView, UserProfileView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registation/', UserCreateView.as_view(), name='registation'),
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
