from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('find_matches', views.find_matches, name='find_matches'),
    path('all_resources', views.all_resources, name='all_resources'),
    path('discussion_forum', views.discussion_forum, name='discussion_forum'),
    path('newPost', views.newPost, name='newPost'),
    path('likePost/<int:id>', views.likePost, name='likePost'),
    path('results', views.results, name='results'),
]