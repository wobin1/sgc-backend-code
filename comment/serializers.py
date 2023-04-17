from rest_framework import serializers
from .models import Comment
from user.serializers import UserSerializer
from newsfeed.serializers import NewsfeedSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        post = serializers.ReadOnlyField()
        posted_by = serializers.ReadOnlyField()
        model = Comment
        fields = [
            'id',
            'post',
            'posted_by',
            'comments',
            'time_posted'
        ]

    def to_representation(self, instance):
        representation = dict()
        representation["id"] = instance.id
        representation["post"] = NewsfeedSerializer(instance.post).data
        representation["posted_by"] = UserSerializer(instance.posted_by).data
        representation["comments"] = instance.comments

        return representation

        def create(self, validated_data):
            comment = Comment(
                post = validated_data['post'],
                posted_by = validated_data['posted_by'],
                comment = validated_data['comment'],
                time_posted = validated_data['time_posted']
            )


            comment.save()
            return comment