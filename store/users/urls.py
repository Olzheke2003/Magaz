from django.urls import path
from users.views import registation, login, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registation/', registation, name='registation'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
