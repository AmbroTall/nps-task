import json

from django.shortcuts import render,redirect
from django.views import csrf
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegisterForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import RegistrationSerializer, AccountPropertiesSerializer, ChangePasswordSerializer, AccountProperties
from .models import Account
from django.conf import settings
import requests

def Login(request):
    context={}
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        loc=request.POST["loc"]
        device=request.POST["dev"]
        osver=request.POST["os"]
        brow=request.POST["brow"]
        ltime=request.POST["time"]
        ipuser=request.POST["ip"]
        mobconn=request.POST["conn"]
        user=Dowell_Login(username,password,loc,device,osver,brow,ltime,ipuser,mobconn)
        print(user)
        x = json.loads(user).get('role')
        try:
            get_jwt = user["jwt"]
            request.COOKIES['access_token'] = get_jwt
            request.session['token'] = get_jwt
            response = render(request, 'voc/nps_index.html')
            response.set_cookie(
                    key = settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value = user["jwt"],
                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            csrf.get_token(request)
            return response
        except:
            if x == "TeamMember" or x == "Admin":
                return redirect("http://127.0.0.1:8000/nps-admin/")
            elif x == "Freelancer" or x == "User":
                return redirect("http://127.0.0.1:8000/nps-scale/default/")
            else:
                return redirect("http://127.0.0.1:8000/nps/login/")
             # return redirect('/')
    return render(request,'account/login_page.html',context)

def Dowell_Login(username,password,location,device,os,browser,time,ip,type_of_conn):
    url="http://100014.pythonanywhere.com/api/login/"
    userurl="http://100014.pythonanywhere.com/api/user/"
    payload = {
        'username': username,
        'password': password,
        'location':location,
        'device':device,
        'os':os,
        'browser':browser,
        'time':time,
        'ip':ip,
        'type_of_conn':type_of_conn
    }
    with requests.Session() as s:
        p = s.post(url, data=payload)
        print(p.text)
        if "Username" in p.text:
            return p.text
        else:
            user = s.get(userurl)
            return user.text

@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def account_info(request):
	try:
		account = request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = AccountProperties(account)
		return Response(serializer.data)