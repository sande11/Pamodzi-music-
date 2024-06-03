from pickle import FALSE
from tkinter import CASCADE
from turtle import st, title
from django.db import models

# Create your models here.


class NewRelease(models.Model):
    title = models.CharField(max_length=250)
    size = models.CharField(max_length=10)
    logo = models.FileField(null=FALSE)
    NewSong = models.FileField(null=FALSE)
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Single(models.Model):
    Singletitle = models.CharField(max_length=250)
    duration = models.CharField(null=FALSE, max_length=10)
    single = models.FileField(null=FALSE)

    def __str__(self):
        return self.Singletitle


class AlbumList(models.Model):
    albumTitle = models.CharField(max_length=250)
    albumArt = models.FileField(null=FALSE)
    albumzip = models.FileField(null=FALSE)

    def __str__(self):
        return self.albumTitle


class AlbumSongs(models.Model):
    albumlist = models.ForeignKey(
        AlbumList, on_delete=models.CASCADE, null=FALSE)
    albumTrack = models.CharField(max_length=250, null=FALSE)
    trackDuration = models.CharField(max_length=10, null=FALSE)
    songs = models.FileField(null=FALSE)

    def __str__(self):
        return self.albumTrack
