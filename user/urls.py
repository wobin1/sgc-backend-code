from django.urls import path
from .views import CreateUser, GetUsers, UpdateUser, UserDetail, SuspendAccount, DeleteUser, OnlineUsersView, NewestMembers, UsersOnline, AccountRequest, AlumniList, Counts


urlpatterns = [
    path('get_users/', GetUsers.as_view()),
    path('get_alumni_list/', AlumniList.as_view()),
    path('create_user/', CreateUser.as_view()),
    path('update_user/<int:id>', UpdateUser.as_view()),
    path('user_detail/<int:id>', UserDetail.as_view()),
    path('suspend_account/<int:id>', SuspendAccount.as_view()),
    path('delete_user/<int:id>', DeleteUser.as_view()),
    path('users_online/', OnlineUsersView.as_view()),
    path('newest_members/', NewestMembers.as_view()),
    path('user_online/', UsersOnline.as_view()),
    path('account_request/', AccountRequest.as_view()),
    path('counts/', Counts.as_view()),

]