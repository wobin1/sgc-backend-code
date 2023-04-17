from rest_framework import serializers
from .models import Newsfeed
from .models import LikedFeed
from user.serializers import UserSerializer



class NewsfeedSerializer(serializers.ModelSerializer):
    class Meta:
        posted_by = serializers.ReadOnlyField()
        liked_by = serializers.ReadOnlyField()
        model = Newsfeed
        fields = [
            'id',
            'posted_by',
            'feed',
            'imageLink',
            'likes_count',
            'time_posted'
        ]

    def to_representation(self, instance):
        representation = dict()
        representation["id"] = instance.id
        representation["posted_by"] = UserSerializer(instance.posted_by).data 
        representation["feed"] = instance.feed
        representation["imageLink"] = instance.imageLink
        representation["likes_count"] = instance.likes_count
        representation["time_posted"] = instance.time_posted

        return representation


        def create(self, validated_data):
            newsfeed = Newsfeed(
                posted_by = validated_data["posted_by"],
                feed = validated_data["feed"],
                image_link = validated_data["image_link"],
                likes_count = validated_data["likes_count"],
            )

            newsfeed.save()
            return newsfeed


class LikedBySerializer(serializers.ModelSerializer):
    class Meta: 
        model= LikedFeed
        fields = [
            'id',
            'post',
            'liked_by'
        ]
    
    def to_representation(self, instance):
        representation= dict()

        representation["id"] = instance.id
        representation["post"] = NewsfeedSerializer(instance.post).data
        representation["like_by"] = UserSerializer(instance.liked_by).data

        def create(self, validated_data):
            likedfeed = LikedFeed(
                post = validated_data["post"],
                liked_by = validated_data["liked_by"]
            )