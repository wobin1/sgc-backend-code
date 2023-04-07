from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Suggestion
from .serializers import SuggestionSerializer



class SuggestionList(APIView):

    def get(self, request):
        suggestions = Suggestion.objects.all()

        serializer = SuggestionSerializer(suggestions, many=True)

        return Response(serializer.data)


class SuggestionCreate(APIView):

    def post(self, request):
        request_data = request.data

        serializer = SuggestionSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({"message": "Suggestion saved", "data": serializer.data})


class SuggestionDetail(APIView):

    def get(self, request, id):
        try:
            suggestion = Suggestion.objects.get(pk=id)
        except Exception as e:
            return Response({"error": str(e)})

        serializer = SuggestionSerializer(suggestion)

        return Response({"data": serializer.data})


class SuggestionDelete(APIView):

    def delete(self, request, id):
        try:
            suggestion = Suggestion.objects.get(pk=id)
        except Exception as e:
            return Response({"error": str(e)})

        suggestion.delete()

        return Response({"message": "Suggestion deleted successfully"})