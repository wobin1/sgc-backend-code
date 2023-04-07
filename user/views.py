from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
import random


class GetUsers(APIView):

    def get(self, request):
        user = User.objects.all()
        print(user)
        serializer = UserSerializer(user, many=True)

        return Response({"data": serializer.data})


class CreateUser(APIView):

    def post(self, request):
        request_data = request.data
        password = request_data["password"]

        otp = random.randint(1000, 9999)
        request_data["otp"] = str(otp)


        serializer = UserSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({"data": serializer.data})

class UpdateUser(APIView):

    def put(self, request, id):
        try:
            user = User.objects.get(pk=id)
            print(user)
        except Exception as e:
            return Response({"error": str(e)})

        request_data = request.data
        request_data["email"] = user.email
        request_data["otp"] = user.otp
        serializer = UserSerializer(user, data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"response": "user updated successfully"})


class SuspendAccount(APIView):

    def put(self, request, id):
        try:
            user = User.objects.get(pk=id)
            print(user)
        except Exception as e:
            return Response({"error": str(e)})

        request_data = request.data
        request_data["first_name"] = user.first_name
        request_data["last_name"] = user.last_name
        request_data["email"] = user.email
        request_data["otp"] = user.otp

        serializer = UserSerializer(user, data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"response": "Account suspended successfully"})

        
        
class UserDetail(APIView):

    def get(self, request, id):
        try:
            user = User.objects.get(pk=id)
        except Exception as e:
            return Response({"erro": str(e)})
        serializer = UserSerializer(user)
        return Response({"data": serializer.data})


class DeleteUser(APIView):

    def delete(self, request, id):
        try:
            user = User.objects.get(pk=id)
            user.delete()
            return Response({"response": "User Deleted successfully"})
        except Exception as e:
            return Response({"erro": str(e)})

            
