# Generated by Django 4.0 on 2022-08-03 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_remove_albumlist_album_album_albumlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Album',
            new_name='AlbumSongs',
        ),
    ]
