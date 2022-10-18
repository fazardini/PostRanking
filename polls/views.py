from django.db.models import Count, Avg
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from polls.models import Post
from polls.serializers import PostSerializer, PollSerializer


class PostList(generics.ListAPIView):

    serializer_class = PostSerializer
    model = serializer_class.Meta.model
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.all().annotate(
            poll_count=Count('polls'))  # .aggregate(score_average=Avg('polls__score'))


class PollCreate(generics.CreateAPIView):
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]
