# Generated by Django 4.0 on 2022-07-29 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_delete_sub_rename_zipfile_album_songs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='albumName',
        ),
    ]