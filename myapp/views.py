from email.mime import base
from fileinput import filename
from http.client import ImproperConnectionState
import imp
import mimetypes
import os
from urllib import response
from wsgiref.util import FileWrapper
from django.forms import FilePathField
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, StreamingHttpResponse
from django.views import View
from . models import NewRelease, Single, AlbumSongs, AlbumList
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'Pamodzi.html')


def music(request):
    newreleases = NewRelease.objects.all
    singles = Single.objects.all
    albumlists = AlbumList.objects.all

    return render(request, 'Page 1.html', {'newreleases': newreleases, 'singles': singles, 'albumlists': albumlists})


def albums(request):
    albumsongs = AlbumSongs.objects.all

    return render(request, 'albums.html', {'albumsongs': albumsongs, })


def events(request):
    return render(request, 'Events.html')


def about(request):
    return render(request, 'about.html')


def downloadfile(req):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = '06_-_Adele_-_Water_Under_The_Bridge-BLUWORLD_Tm99zos.mp3'
    filepath = base_dir + '/media/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 9.21
    response = StreamingHttpResponse(FileWrapper(
        open(thefile, 'rb'), chunk_size), content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;filename=%s" % filename
    return response
