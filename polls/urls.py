from django.urls import path

from polls.views import PostList, PollCreate

urlpatterns = [
    path('posts/', PostList.as_view(), name='view_posts'),
    path('poll/', PollCreate.as_view(), name='create_poll')
]
