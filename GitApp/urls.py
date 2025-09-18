from django.urls import path
from .views import FetchGitHubUser, GetGitHubUserFromDB, FetchRepositoriesFromDB

urlpatterns = [
    path('fetch-user/', FetchGitHubUser.as_view(), name="fetch_user"),
    path('user/<str:username>/', GetGitHubUserFromDB.as_view(), name="get_user"),
    path('user/<str:username>/repos/', FetchRepositoriesFromDB.as_view(), name="get_repos"),
]
