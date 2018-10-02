from django import forms
from .models import *

class GithubUserForm(forms.ModelForm):
    class Meta:
        model = GithubUser
        fields = ["name", "blog", "public_gists", "public_repos", "avatar_url", "followers", "following", "location"]   # nessesary
        exclude = [""]  # exception
