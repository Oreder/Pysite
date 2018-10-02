from django.db import models

class GithubUser(models.Model):
    name = models.CharField(null=True, max_length=128)
    blog = models.CharField(null=True, max_length=128)
    public_gists = models.IntegerField(default=0)
    public_repos = models.IntegerField(default=0)
    avatar_url = models.URLField()
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    location = models.CharField(null=True, max_length=256)
