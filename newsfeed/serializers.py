from rest_framework import serializers
from .models import Newsfeed
from user.serializers import UserSerializer



class NewsfeedSerializer(serializers.ModelSerializer):
    class Meta:
        posted_by = serializers.ReadOnlyField()
        model = Newsfeed
        fields = [
            'id',
            'posted_by',
            'feed',
            'imageLink',
            'likes'
            'time_posted'
        ]

    def to_representation(self, instance):
        representation = dict()
        representation["id"] = instance.id
        representation["posted_by"] = UserSerializer(instance.posted_by).data 
        representation["feed"] = instance.feed
        representation["imageLink"] = instance.imageLink
        representation["likes"] = instance.likes
        representation["time_posted"] = instance.time_posted

        return representation


        def create(self, validated_data):
            newsfeed = Newsfeed(
                posted_by = validated_data["posted_by"],
                feed = validated_data["feed"],
                image_link = validated_data["image_link"],
                likes = validated_data["likes"]

            )

            newsfeed.save()
            return newsfeed