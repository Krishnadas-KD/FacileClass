from main.models import user_info
from teachl.models import *
from .models import *
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.api import error
from django.contrib import messages 

global popupurl

def userp(response):
    email = response.session['mail']
    ls = sroominfo.objects.filter(Email=email)
    context = {
        'ls':ls
    }
    return render(response,"upage.html",{'context':context})
    

    
def logout(response):
    response.session.flush()
    return HttpResponseRedirect('/')
    
def createclass_form(request):
    return render(request,"addpage.html")


def createclass(request):
    mail = request.session['mail']
    if request.method == 'POST':
        if request.POST.get('add'):
            classname = request.POST.get('clsname')
            if roominfo.objects.filter(Roomcode=classname).exists():
                ls=roominfo.objects.get(Roomcode=classname)
                to = sroominfo(Email=mail,Roomcode=ls.Roomcode,roomname=ls.roomname,url=ls.url,roomdesc=ls.roomdesc)
                to.save()
            else:
                messages.error(request,'Incorrept code')
        
            return redirect('/')
        return redirect('/')
    return redirect('/')



def classwork(requset,cod):
     tk = requset.session['mail']
     if user_info.objects.filter(Email=tk).exists():
          if roominfo.objects.filter(url=cod).exists():
               
               rcod=roominfo.objects.get(url=cod)
               print('\n',rcod.Roomcode,'\n')
               if not popupurl== '0':
                    context={
                         'url':cod,
                         'rcode':rcod.Roomcode,
                         "pdf":contends.objects.filter(RoomCode=cod),
                         "ls":code.objects.filter(RoomCode=cod),
                         "yt":youtubelink.objects.filter(RoomCode=cod),
                         "link":otherlink.objects.filter(RoomCode=cod),
                         "popuplink":popupurl
                         }
               else:
                    context={
                         'url':cod,
                         'rcode':rcod,
                         "pdf":contends.objects.filter(RoomCode=cod),
                         "ls":code.objects.filter(RoomCode=cod),
                         "yt":youtubelink.objects.filter(RoomCode=cod),
                         "link":otherlink.objects.filter(RoomCode=cod)
                         }
               return render(requset, "classwork.html",{'context':context})

def prople(requset,cod):
     tk = requset.session['mail']
     if user_info.objects.filter(Email=tk).exists():
          if roominfo.objects.filter(url=cod).exists():
               rcod=roominfo.objects.get(url=cod)
               print(sroominfo.objects.filter(Roomcode=cod))
               context={
                         'url':cod,
                         'rcode':rcod,
                         "student":sroominfo.objects.filter(Roomcode=rcod.Roomcode),


                         }
               return render(requset, "people.html",{'context':context})