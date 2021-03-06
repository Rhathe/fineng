# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import HttpResponse
from models import *

def login_user(request):
    # get CSRF token
    c = {}
    c.update(csrf(request))

    state = "Please log in below..."
    returnsite = 'auth.html'
    username = password = ''
    stockset = Stock.objects.all()
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                returnsite = 'main.html'
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response(returnsite,{'state':state, 'username': username, 'stockset': stockset},context_instance=RequestContext(request))

def logout_user(request):
	logout(request)
	return redirect('/')
