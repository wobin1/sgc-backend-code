from django.urls import path
from .views import UserLogin, VerifyEmail, ForgotPassword, ResetPassword



urlpatterns = [
    path("login/", UserLogin.as_view()),
    path("verify_email/<int:id>", VerifyEmail.as_view()),
    path("forgot_password/", ForgotPassword.as_view()),
    path("reset_password/<int:id>", ResetPassword.as_view())
]