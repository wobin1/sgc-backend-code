from django.shortcuts import render
from django.conf import settings
from user.models import User
from user.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from django.core.mail import send_mail



class UserLogin(APIView):

    def post(self, request):
        request_data = request.data

        try:
            user = User.objects.get(email=request_data["email"])
        except User.DoesNotExist:
            return Response({"erro": "Invalid Email"})

        if not user.check_password(request_data["password"]):
            return Response({"error": "invalid password"})

        refresh = RefreshToken.for_user(user)
        token = {
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token)
        }

        # Serializer user data and token
        data =UserSerializer(user).data
        data['token'] = token
        print("this endpoint is working")

        request_data["first_name"] = user.first_name
        request_data["last_name"] = user.last_name
        request_data["email"] = user.email
        request_data["date_of_birth"] = user.date_of_birth
        request_data["otp"] = user.otp
        request_data["password"] = user.password
        request_data["is_online"] = True
        print(request_data)

        serializer = UserSerializer(user, data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)

        # response["Access-Control-Allow-Origin"] = '*'
        # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
        # response["Access-Control-Max-Age"] = '1000'
        # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
        response = Response({"message": "login successful", "data": data})

        return response
        

class VerifyEmail(APIView):

    def put(self, request, id):
        request_data = request.data

        try:
            user = User.objects.get(pk=id)
        except Exception as e:
            return Response({"error": str(e)})

        if request_data.get("otp") == user.otp:
            request_data["first_name"] = user.first_name
            request_data["last_name"] = user.last_name
            request_data["email"] = user.email
            request_data["password"] = user.password
            request_data["token_used"] = True
            request_data["is_verified"] = True

            serializer = UserSerializer(user, data=request_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                # response["Access-Control-Allow-Origin"] = '*'
                # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
                # response["Access-Control-Max-Age"] = '1000'
                # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
                response = Response({"data": serializer})
                return response

        else:
            # response["Access-Control-Allow-Origin"] = '*'
            # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
            # response["Access-Control-Max-Age"] = '1000'
            # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            response = Response({"error": "invalid otp"})

            return response


class ForgotPassword(APIView):

    def put(self, request):
        request_data = request.data
        try:
            user = User.objects.get(email=request_data.get("email"))
        except Exception as e:
            return Response({"error": str(e)})

        if user.email == request_data.get("email"):
            otp = str(random.randint(1000,9999))
            request_data["first_name"] = user.first_name
            request_data["last_name"] = user.last_name
            request_data["password"] = user.password
            request_data["otp"] = otp
            request_data["token_used"] = False

            serializer = UserSerializer(user, data=request_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

            subject = 'Forgot password OTP'
            first_name = serializer.data.get('firstname')
            email = serializer.data.get('email')
            message = f'Use the OTP to reset your password {otp}'
            sender = settings.EMAIL_HOST_USER
            recipient_list = [email]  

            # send_email(subject, message, sender, recipient_list)

            # response["Access-Control-Allow-Origin"] = '*'
            # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
            # response["Access-Control-Max-Age"] = '1000'
            # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            response = Response({"data": serializer})

            response = Response({"message": "A OTP has been send to your email use it to reset password", "data": serializer.data})

            return response


class ResetPassword(APIView):

    def put(self, request, id):
        request_data = request.data
        try:
            user = User.objects.get(pk=id)
        except Exception as e:
            return Response({"error": str(e)})

        password = request_data.get("password")

        user.set_password(password)

        request_data["first_name"] = user.first_name
        request_data["last_name"] = user.last_name
        request_data["email"] = user.email
        request_data["otp"] = user.otp
        request_data["password"] = user.password

        serializer = UserSerializer(user, data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


            # response["Access-Control-Allow-Origin"] = '*'
            # response["Access-Control-Allow-Methods"] = 'GET,PUT, OPTIONS'
            # response["Access-Control-Max-Age"] = '1000'
            # response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            response = Response({"data": serializer})
            
            return response



class Logout(APIView):
    def get(self, request, id):
        request_data = request.data
        try:
            user = User.objects.get(pk=id)
        except Exception as e:
            return Response({"erro": str(e)})

        data =UserSerializer(user).data
        print("this endpoint is working")

        request_data["first_name"] = user.first_name
        request_data["last_name"] = user.last_name
        request_data["email"] = user.email
        request_data["date_of_birth"] = user.date_of_birth
        request_data["otp"] = user.otp
        request_data["password"] = user.password
        request_data["is_online"] = False


        serializer = UserSerializer(user, data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)


        response = Response({"message": "User logged out successfully"})

        return response