from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Newsfeed
from .serializers import NewsfeedSerializer


class NewsfeedList(APIView):
    def get(self, request):
        newsfeeds = Newsfeed.objects.all()

        serializer = NewsfeedSerializer(newsfeeds, many=True)
        return Response({"data": serializer.data})

class NewsfeedCreate(APIView):
    def post(self, request):
        request_data = request.data

        serializer = NewsfeedSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({"message": "feed created successfully", "data": serializer.data})


class NewsfeedDetail(APIView):
    def get(self, request, id):
        try:
            feed = Newsfeed.objects.get(pk=id)
        except Exception as e:
            return Response({"error": str(e)})

        serializer = NewsfeedSerializer(feed)

        return Response({"data": serializer.data})


class NewsfeedDelete(APIView):
    def delete(self, request, id):
        try:
            feed = Newsfeed.objects.get(pk=id)
        except Exception as e:
            return Response({"error": str(e)})

        feed.delete()

        return Response({"message": "feed deleted successfully"})

