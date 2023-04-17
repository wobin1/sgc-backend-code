from django.urls import path
from .views import CommentList, CommentCreate



urlpatterns = [
    path("comment_list/", CommentList.as_view()),
    path("comment_create/", CommentCreate.as_view())
]