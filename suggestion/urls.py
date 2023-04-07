from django.urls import path
from .views import SuggestionCreate, SuggestionList, SuggestionDetail, SuggestionDelete


urlpatterns = [
    path('create_suggestion/', SuggestionCreate.as_view()),
    path('list_suggestion/', SuggestionList.as_view()),
    path('detail_suggestion/<int:id>', SuggestionDetail.as_view()),
    path('delete_suggestion/<int:id>', SuggestionDelete.as_view())
]