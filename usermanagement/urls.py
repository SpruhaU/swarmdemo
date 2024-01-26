from django.urls import path
from .views import user_list, add_user ,home

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('add/', add_user, name='add_user'),
     path('', home, name='home'),
]