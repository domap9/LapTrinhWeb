from os import name
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.songs, name="songs"),
    path('songs/<int:id>', views.songpost, name="songpost"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('watchlater/',views.watchlater, name="watchlater"),
    path('history/',views.history,name="history"),
    path('c/<str:channel>',views.channel,name="channel"),
    path('upload/',views.upload,name="upload"),
    path('search/',views.search,name="search"),
    path('category/<int:id>/<slug:slug>', views.category_music, name='category_music'),
    path('song_channel/<int:id>',views.songpost_channel, name="songpost_channel"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('delete_channel/<int:id1>',views.delete_channel,name="delete_channel"),
    path('rank/',views.rank,name="rank"),

]
