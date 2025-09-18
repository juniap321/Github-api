import requests
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import GitHubUser, GitHubRepository
from .serializers import GitHubUserSerializer, GitHubRepositorySerializer

GITHUB_USER_API = "https://api.github.com/users/{}"
GITHUB_REPOS_API = "https://api.github.com/users/{}/repos"


class FetchGitHubUser(APIView):
    def post(self, request):
        username = request.data.get("username")
        if not username:
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch user profile
        user_response = requests.get(GITHUB_USER_API.format(username))
        if user_response.status_code == 404:
            return Response({"error": "Invalid GitHub username"}, status=status.HTTP_404_NOT_FOUND)
        if user_response.status_code != 200:
            return Response({"error": "GitHub API error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        user_data = user_response.json()

        user, created = GitHubUser.objects.update_or_create(
            username=user_data["login"],
            defaults={
                "name": user_data.get("name"),
                "public_repos_count": user_data.get("public_repos", 0),
                "followers_count": user_data.get("followers", 0),
                "following_count": user_data.get("following", 0),
                "account_creation_date": user_data.get("created_at"),
            }
        )

        # Fetch repositories
        repo_response = requests.get(GITHUB_REPOS_API.format(username))
        if repo_response.status_code == 200:
            repos = repo_response.json()
            for repo in repos:
                GitHubRepository.objects.update_or_create(
                    user=user,
                    name=repo["name"],
                    defaults={
                        "primary_language": repo.get("language"),
                        "star_count": repo.get("stargazers_count", 0),
                        "fork_count": repo.get("forks_count", 0),
                        "last_updated_date": repo.get("updated_at"),
                    }
                )

        serializer = GitHubUserSerializer(user)
        return Response(serializer.data)


class GetGitHubUserFromDB(APIView):
    def get(self, request, username):
        user = get_object_or_404(GitHubUser, username=username)
        serializer = GitHubUserSerializer(user)
        return Response(serializer.data)


class FetchRepositoriesFromDB(APIView):
    def get(self, request, username):
        user = get_object_or_404(GitHubUser, username=username)
        repos = user.repositories.all()
        serializer = GitHubRepositorySerializer(repos, many=True)
        return Response(serializer.data)
