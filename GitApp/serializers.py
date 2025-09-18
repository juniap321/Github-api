from rest_framework import serializers
from .models import GitHubUser, GitHubRepository

class GitHubRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubRepository
        fields = ['id', 'name', 'primary_language', 'star_count', 'fork_count', 'last_updated_date']

class GitHubUserSerializer(serializers.ModelSerializer):
    repositories = GitHubRepositorySerializer(many=True, read_only=True)

    class Meta:
        model = GitHubUser
        fields = [
            'id', 'username', 'name', 'public_repos_count',
            'followers_count', 'following_count', 'account_creation_date',
            'repositories'
        ]
