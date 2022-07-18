import random
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializer import SystemSettingsSerializer, ResponseSerializer
from .models import system_settings, response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication


class SystemSettings(viewsets.ModelViewSet):
    serializer_class = SystemSettingsSerializer
    queryset = system_settings.objects.all()
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

class Response(viewsets.ModelViewSet):
    serializer_class = ResponseSerializer
    queryset = response.objects.all()

# @login_required
# def dowell_scale_admin(request):
#     context={}
#     user=request.user
#     role=Scale_user(user)
#     if role=="Admin" or role=="TeamMember":
#         if request.method == 'POST':
#             name = request.POST['nameofscale']
#             orientation = request.POST['orientation']
#             numberrating  = request.POST['numberof']
#             scalecolor  = request.POST['scolor']
#             roundcolor  = request.POST['rcolor']
#             fontcolor  = request.POST['fcolor']
#             fomat  = request.POST['format']
#             left=request.POST["left"]
#             right=request.POST["right"]
#             center=request.POST["center"]
#             time = request.POST['time']
#             text=f"{left}+{center}+{right}"
#             rand_num = random.randrange(1,10000)
#             template_name = f"{name}{rand_num}"
#             r=Scale(role,orientation,scalecolor,roundcolor,fontcolor,fomat,numberrating,time,template_name,text,name)
#             objcolor = models.Rating.objects.create(orientation=orientation,rating=numberrating,scolor=scalecolor,rcolor=roundcolor,fcolor=fontcolor,format=fomat,time=time,template_name=template_name,name=name,text=text)
#             objcolor.save()
#             if r=="success":
#                 return redirect(f"https://100014.pythonanywhere.com/nps/dowellscale/{template_name}")
#             else:
#                 context["Error"]="Error Occured while save the custom pl contact admin"
#         return render(request,'voc/scale_admin.html',context)
#     else:
#         return redirect("https://100014.pythonanywhere.com/nps/dowellscale/default")
#     # context["url"]="/scaleadmin"
#     # context["urltext"]="Create new scale"
#

@login_required
def dowell_scale_admin(request):
    context={}
    user = request.user
    role = user.role
    if role == "Admin" or role == "TeamMember":
        if request.method == 'POST':
            name = request.POST['nameofscale']
            orientation = request.POST['orientation']
            numberrating = request.POST['numberof']
            scalecolor = request.POST['scolor']
            roundcolor = request.POST['rcolor']
            fontcolor = request.POST['fcolor']
            fomat = request.POST['format']
            left = request.POST["left"]
            right = request.POST["right"]
            center = request.POST["center"]
            time = request.POST['time']
            text = f"{left}+{center}+{right}"
            rand_num = random.randrange(1, 10000)
            template_name = f"{name.replace(' ', '')}{rand_num}"
            # r = system_settings(orientation, scalecolor, roundcolor, fontcolor, fomat, numberrating, time, template_name, text, name)
            objcolor = system_settings.objects.create(orientation=orientation,numberrating=numberrating,scalecolor=scalecolor,roundcolor=roundcolor,fontcolor=fontcolor,fomat=fomat,time=time,template_name=template_name,name=name,text=text, left=left,right=right,center=center)
            objcolor.save()
            if objcolor != "":
                # return redirect(f"https://100014.pythonanywhere.com/nps/dowellscale/{template_name}")
                return redirect(f"http://127.0.0.1:8000/nps-scale/{template_name}")
            else:
                context["Error"] = "Error Occurred while save the custom pl contact admin"
        return render(request, 'nps/scale_admin.html', context)
    else:
        # return redirect("https://100014.pythonanywhere.com/nps/dowellscale/default")
        return redirect(f'http://127.0.0.1:8000/nps-scale/default/')


def dowell_scale(request,tname):
    context={}
    context["url"]="../scaleadmin"
    context["urltext"]="Create new scale"
    context["btn"]="btn btn-dark"
    context["hist"]="Scale History"
    context["bglight"]="bg-light"
    context["left"]="border:silver 2px solid; box-shadow:2px 2px 2px 2px rgba(0,0,0,0.3)"
    context["npsall"]=system_settings.objects.all().order_by('-id')
    default=system_settings.objects.filter(template_name=tname)
    context["defaults"]=default
    for i in default:
        context["text"]=i.text.split('+')
        print(i)
    return render(request,'nps/scale.html',context)


def default_scale(request):
    return render(request, 'nps/default.html')


# def Dowell_Login(username,password,location,device,os,browser,time,ip,type_of_conn):
#     url="http://127.0.0.1:8000/login/"
#     userurl="http://127.0.0.1:8000//user/"
#     # url="http://100014.pythonanywhere.com/api/login/"
#     # userurl="http://100014.pythonanywhere.com/api/user/"
#     payload = {
#         'username': username,
#         'password': password,
#         'location':location,
#         'device':device,
#         'os':os,
#         'browser':browser,
#         'time':time,
#         'ip':ip,
#         'type_of_conn':type_of_conn
#     }
#     with requests.Session() as s:
#         p = s.post(url, data=payload)
#         print(p.text)
#         if "Username" in p.text:
#             return p.text
#         else:
#             user = s.get(userurl)
#             return user.text