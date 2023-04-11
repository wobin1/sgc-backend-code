from django.urls import path
from .views import CreateUser, GetUsers, UpdateUser, UserDetail, SuspendAccount, DeleteUser, OnlineUsersView


urlpatterns = [
    path('get_users/', GetUsers.as_view()),
    path('create_user/', CreateUser.as_view()),
    path('update_user/<int:id>', UpdateUser.as_view()),
    path('user_detail/<int:id>', UserDetail.as_view()),
    path('suspend_account/<int:id>', SuspendAccount.as_view()),
    path('delete_user/<int:id>', DeleteUser.as_view()),
    path('users_online/', OnlineUsersView.as_view())

]