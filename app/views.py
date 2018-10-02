from django.shortcuts import render
import requests
from .forms import *
from .models import *

def SrcToInt(source):
	value = 0
	if source != "":
		value = int(source)
	return value

def SrcToChar(source):
    value = ""
    if source != None:
        value = source
    return value

# Create your views here.
def index(request):
    parsedData = []
    if request.method == 'POST':
        user = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + user)

        jsonList = []
        jsonList.append(req.json())
        userData = {}

		# show in page
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
            userData['location'] = data['location']
            parsedData.append(userData)

        # Save to model
        gUser = GithubUser()
        gUser.name = SrcToChar(data['name'])
        gUser.blog = SrcToChar(data['blog'])
        gUser.public_gists = SrcToInt(data['public_gists'])
        gUser.public_repos = SrcToInt(data['public_repos'])
        gUser.avatar_url = data['avatar_url']
        gUser.followers = SrcToInt(data['followers'])
        gUser.following = SrcToInt(data['following'])
        gUser.location = SrcToChar(data['location'])
        gUser.save()
    return render(request, "app/index.html", {'data': parsedData})