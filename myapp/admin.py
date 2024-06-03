from tokenize import Single
from django.contrib import admin
from . models import AlbumSongs, NewRelease,Single, AlbumSongs,AlbumList

# Register your models here.
admin.site.register(NewRelease)
admin.site.register(Single)
admin.site.register(AlbumSongs)
admin.site.register(AlbumList)