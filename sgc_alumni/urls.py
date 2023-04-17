from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/suggestion/', include('suggestion.urls')),
    path('api/feed/', include('newsfeed.urls')),
    path('api/comment/', include('comment.urls')),
]
