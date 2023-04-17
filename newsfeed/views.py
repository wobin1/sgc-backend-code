from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from newsfeed.models import Newsfeed
from newsfeed.serializers import NewsfeedSerializer
from .models import User
from .models import LikedFeed
from comment.models import Comment
from .serializers import NewsfeedSerializer
from .serializers import LikedBySerializer
from comment.serializers import CommentSerializer
from user.serializers import UserSerializer
from django.utils.timezone import now

class NewsfeedList(APIView):
    def get(self, request):
        newsfeeds = Newsfeed.objects.all()
        response_data = []

        serializer = NewsfeedSerializer(newsfeeds, many=True)

        for item in serializer.data:
            post_id = item["id"]
            print(item)
            print(post_id)
            query = Comment.objects.filter(post=post_id)
            commentserializer = CommentSerializer(query, many=True)
            item["comments"] = commentserializer.data
            response_data.append(item)

        # response=''

        # response["Access-Control-Allow-Origin"] = '*'
        # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
        # response["Access-Control-Max-Age"] = '1000'
        # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
        response = Response({"data": response_data})

        return response

class NewsfeedCreate(APIView):
    def post(self, request, id):
        request_data = request.data

        serializer = NewsfeedSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


            # response["Access-Control-Allow-Origin"] = '*'
            # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
            # response["Access-Control-Max-Age"] = '1000'
            # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            response = Response({"message": "feed created successfully", "data": serializer.data})
            return response


class NewsfeedDetail(APIView):
    def get(self, request, id):
        try:
            feed = Newsfeed.objects.get(pk=id)
        except Exception as e:

            # response["Access-Control-Allow-Origin"] = '*'
            # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
            # response["Access-Control-Max-Age"] = '1000'
            # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            response = Response({"error": str(e)})
            return response

        serializer = NewsfeedSerializer(feed)

        return Response({"data": serializer.data})


class NewsfeedDelete(APIView):
    def delete(self, request, id):
        try:
            feed = Newsfeed.objects.get(pk=id)
        except Exception as e:
            return Response({"error": str(e)})

        feed.delete()
        # response["Access-Control-Allow-Origin"] = '*'
        # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
        # response["Access-Control-Max-Age"] = '1000'
        # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
        response = Response({"message": "feed deleted successfully"})

        return response



@api_view(['PUT'])
def like(request, id, format=None):
    request_data = request.data
    post_id = request_data["post_id"]
    try:
        user = User.objects.get(pk=id)
        feed = Newsfeed.objects.get(id=post_id)
    except Exception as e:
        return Response({"error": str(e)})

    user_data = UserSerializer(user)
    liked = LikedFeed.objects.filter(post=post_id)
    if id in liked:
        # when user already like post
        return Response({"message": 'You have already liked this post'})
    else:
        print("breaker1")
        liked = LikedFeed.objects.get(id=post_id)
        print(liked)

        print("breaker2")

        feedlike = {}
        feedlike["post"] = post_id
        feedlike["liked_by"] = id

        # print(feedlike)
        # likedserializer = LikedBySerializer(data=feedlike)
        # if likedserializer.is_valid(raise_exception=True):
        #     likedserializer.save()

        feed = Newsfeed.objects.get(id=post_id)
        feedData =NewsfeedSerializer(feed).data
        print("feed data")
        print(feedData)
        request_data["likes_count"] = feedData.get('likes_count') + 1
        request_data["posted_by"] = feedData.get('posted_by').id
        request_data["feed"] = feedData.get('feed')
        request_data["imageLink"] = feedData.get('imageLink')

        feedSerializer =NewsfeedSerializer(data=request_data)
        if feedSerializer.is_valid(raise_exception=True):
            feedSerializer.save()
           
    response = Response({"message": "successfully liked"})

    return response

