from django.db import models

class GitHubUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    public_repos_count = models.IntegerField(default=0)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    account_creation_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'github_users'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.username} - {self.name or 'No Name'}"


class GitHubRepository(models.Model):
    user = models.ForeignKey(GitHubUser, on_delete=models.CASCADE, related_name='repositories')
    name = models.CharField(max_length=200)
    primary_language = models.CharField(max_length=50, blank=True, null=True)
    star_count = models.IntegerField(default=0)
    fork_count = models.IntegerField(default=0)
    last_updated_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'github_repositories'
        ordering = ['-star_count', '-last_updated_date']
        unique_together = ['user', 'name']

    def __str__(self):
        return f"{self.user.username}/{self.name}"
