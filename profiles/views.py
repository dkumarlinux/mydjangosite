from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
#	context= locals()
	context= {}
	template='home.html'
	return render(request, template, context)

def about(request):
#	context= locals()
	context= {'about':["Hi I am from views's dictionery method first value..",
			  "Hi I am from views's dictionery method second value" ]}
	template='about.html'
	return render(request, template, context)

@login_required
def userProfile(request):
	user = request.user
#	context= locals()
	context= {'user':user}
	template='profile.html'
	return render(request, template, context)