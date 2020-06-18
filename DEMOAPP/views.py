from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
import os
import os.path
from . import  pafy
from . import youtube_dl
from pafy import backend_youtube_dl
from . import pytube
from pytube import YouTube
from django.core import mail
from django.core.mail import send_mail



# Create your views here.

def down(request):
    resolutions = []
    sourc= ''
    result= ''
    lnk = ''
    global url
    url = ''
    if request.method == "POST":
        url = request.POST.get('link')
        correct_url = url
        if 'm.' in url:
            correct_url = correct_url.replace('m.', '')
        if 'youtu.be' in url:
            video_id = url.split('/')[-1]
            correct_url = 'https://www.youtube.com/watch?v=' + video_id
        url = correct_url
        lnk = pafy.new(url)
        strmall = lnk.streams
        for i in strmall:
            resolutions.append(i.resolution)
        resolutions = list(dict.fromkeys(resolutions))
        n = len(resolutions)
        result=url.find("watch?v=")
        if(result):
            sourc = url.replace("watch?v=", "embed/")
            sourc = sourc.replace(".com/embed/", ".com/")
        sourc = sourc.replace(".com/", ".com/embed/")
    return render(request, 'prjct.html', {'rsl':resolutions,'source':sourc})



def yt_down(request):
    titl = ''
    cwd = ''
    directory = "InsTube"
    urlcpy = ''
    result = "result.mp4"
    if request.method == "POST":
        urlcpy = request.POST.get('quality')
        urlcpy = urlcpy.replace("embed/", "watch?v=")
        dl = pafy.new(urlcpy)
        titl = dl.title
        full= titl + ".mp4"
        return render(request, 'download.html', {'title':titl,'dirs':cwd})
    else:
        return render(request,'googlerobot.html')


def  feedback(request):
    msg = ' '
    nme = ' '
    try:
        if request.method == "POST":
            nme = request.POST.get('1')
            msg = request.POST.get('2')
            send_mail(
                 nme,
                 msg,
                'gameboytestmail@gmail.com',
                ['kv2002975@gmail.com'],
                fail_silently=False,
            )
            return request(request, 'feedback.html')
        return request(request, 'prjct.html')
    except:
        return render(request, 'googlerobot.html')