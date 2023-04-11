from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Newsfeed
from .serializers import NewsfeedSerializer
from django.utils.timezone import now

class NewsfeedList(APIView):
    def get(self, request):
        newsfeeds = Newsfeed.objects.all()

        serializer = NewsfeedSerializer(newsfeeds, many=True)

        response["Access-Control-Allow-Origin"] = '*'
        response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
        response["Access-Control-Max-Age"] = '1000'
        response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
        response = Response({"data": serializer.data})

        return response

class NewsfeedCreate(APIView):
    def post(self, request, id):
        request_data = request.data

        serializer = NewsfeedSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


            response["Access-Control-Allow-Origin"] = '*'
            response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            response = Response({"message": "feed created successfully", "data": serializer.data})
            return response


class NewsfeedDetail(APIView):
    def get(self, request, id):
        try:
            feed = Newsfeed.objects.get(pk=id)
        except Exception as e:

            response["Access-Control-Allow-Origin"] = '*'
            response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
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

        return Response({"message": "feed deleted successfully"})

