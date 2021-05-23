from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('added',views.added,name ='added'),
    path('leaderboard',views.leaderboard,name ='leaderboard')


]
