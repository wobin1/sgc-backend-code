from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from django.utils.timezone import now


class CommentList(APIView):
    
    def get(self, request):
        comment = Comment.objects.all()

        serializer = CommentSerializer(comment, many=True)

        response = Response({"data": serializer.data})

        return response


class CommentCreate(APIView):

    def post(self, request):
        request_data = request.data

        serializer = CommentSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        response = Response({"message": "comment added successfully", "data": serializer.data})

        return response




