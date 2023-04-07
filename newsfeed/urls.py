from django.urls import path
from .views import NewsfeedCreate, NewsfeedList, NewsfeedDetail, NewsfeedDelete


urlpatterns = [
    path('create_newsfeed/', NewsfeedCreate.as_view()),
    path('list_newsfeed/', NewsfeedList.as_view()),
    path('detail_newsfeed/<int:id>', NewsfeedDetail.as_view()),
    path('delete_newsfeed/<int:id>', NewsfeedDelete.as_view())
]