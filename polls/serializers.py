from rest_framework import serializers

from polls.models import Post, Poll


class PostSerializer(serializers.ModelSerializer):
    poll_count = serializers.IntegerField(read_only=True)
    score_average = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'poll_count', 'score_average', )


class PollSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='id')

    class Meta:
        model = Poll
        fields = ('post', 'score')

    def validate(self, data):
        score = data['score']
        if not (-1 < score < 6):
            raise serializers.ValidationError('Invalid score ...!!!')
        return data

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        post = validated_data.get('post')
        score = validated_data.get('score')
        poll, created = Poll.objects.update_or_create(post=post, user=user,
                                                      defaults={'score': score})
        return poll
