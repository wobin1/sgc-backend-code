from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
import random
from datetime import timedelta
from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTAuthentication



class GetUsers(APIView):

    def get(self, request):
        user = User.objects.all().order_by('first_name')
        print(user)
        serializer = UserSerializer(user, many=True)

        # response["Access-Control-Allow-Origin"] = '*'
        # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
        # response["Access-Control-Max-Age"] = '1000'
        # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
        response = Response({"data": serializer.data})
        return response


class CreateUser(APIView):

    def post(self, request):
        request_data = request.data
        password = request_data["password"]

        otp = random.randint(1000, 9999)
        request_data["otp"] = str(otp)


        serializer = UserSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            # response["Access-Control-Allow-Origin"] = '*'
            # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
            # response["Access-Control-Max-Age"] = '1000'
            # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            response = Response({"data": serializer.data})
            return response

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

class AlumniList(APIView):
     def get(self, request):
        user = User.objects.filter(is_staff=False)[:10]
        print(user)
        serializer = UserSerializer(user, many=True)

        return Response({"data": serializer.data})      
        
class UserDetail(APIView):

    def get(self, request, id):
        try:
            user = User.objects.get(pk=id)
        except Exception as e:
            return Response({"erro": str(e)})
        serializer = UserSerializer(user)

        # response["Access-Control-Allow-Origin"] = '*'
        # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
        # response["Access-Control-Max-Age"] = '1000'
        # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
        response = Response({"data": serializer.data})
        return response


class DeleteUser(APIView):

    def delete(self, request, id):
        try:
            user = User.objects.get(pk=id)
            user.delete()

            # response["Access-Control-Allow-Origin"] = '*'
            # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
            # response["Access-Control-Max-Age"] = '1000'
            # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            response = Response({"response": "User Deleted successfully"})
            return response
        except Exception as e:
            return Response({"erro": str(e)})

            
class OnlineUsersView(APIView):
    jwt_auth = JWTAuthentication()

    def get(self, request):

        # get the current time
        now = timezone.now()

        # calculate the cutoff time for active users
        cutoff = now - timedelta(minutes=5)

        # filter the users who have been active within the last 5 minutes
        active_users = User.objects.filter(last_seen_gte=cutoff)

        # return a list of active user IDS and email

        data = [
            {
                'id': user.id,
                'email': user.email
            }
            for user in active_users
        ]

        return Response(data)


class NewestMembers(APIView):
    def get(self, request):
        user = User.objects.all().order_by('-user_created_at')[:5]
        print(user)
        serializer = UserSerializer(user, many=True)

        # response["Access-Control-Allow-Origin"] = '*'
        # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
        # response["Access-Control-Max-Age"] = '1000'
        # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
        response = Response({"data": serializer.data})
        return response


class UsersOnline(APIView):
    def get(self, request):
        user = User.objects.filter(is_online=True)[:5]
        print(user)
        serializer = UserSerializer(user, many=True)

        return Response({"data": serializer.data})


class UsersOnline(APIView):
    def get(self, request):
        user = User.objects.filter(is_online=True)[:5]
        print(user)
        serializer = UserSerializer(user, many=True)

        return Response({"data": serializer.data})

class AccountRequest(APIView):
    def get(self, request):
        user = User.objects.filter(is_approved=False)[:10]
        print(user)
        serializer = UserSerializer(user, many=True)

        return Response({"data": serializer.data})

class ApproveAccountRequest(APIView):
    def put(self, request, id):
        request_data = request.data
        print(request_data)
        try:
            user = User.objects.get(pk=id)
            print(user.first_name)
        except Exception as e:
            return Response({"error": str(e)})

        data = UserSerializer(user).data
        # print(data["password"])

        request_data["first_name"] = data["first_name"]
        request_data["last_name"] = data["last_name"]
        request_data["email"] = data["email"]
        request_data["otp"] = data["otp"]
        request_data["password"] = data["password"]

        print(request_data)

        serializer = UserSerializer(user, data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        response = Response({"message": "Account approved"})

        return response

class Counts(APIView):
    def get(self, request):
        total_account = User.objects.all().count()
        account_pending = User.objects.filter(is_approved=False).count()
        account_approved = User.objects.filter(is_approved=True).count()
        
        response = {"total_account": total_account,
                        "account_pending": account_pending,
                        "account_approved": account_approved
                    }
        

        return Response({"data": response})