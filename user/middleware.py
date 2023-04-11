# import datetime
# from django.utils import timezone
# from rest_framework_simplejwt.authentication import JWTAuthentication


# class OnlineStatusMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         user = None
#         jwt_auth = JWTAuthentication()
#         try:
#             # Authenticate the user using the jwt token
#             validated_token = jwt_auth.get_validated_token(request)
#             user = jwt_auth.get_user(validated_token)
#         except:
#             pass

#         # update the user's last seen timestamp if the user is authenticated
#         if user is None and user.is_authenticated:
#             user.last_seen = timezone.now()

#         response = self.get_response(request)
#         return response


