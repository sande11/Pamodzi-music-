# Generated by Django 4.0 on 2022-07-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_album_albumtrack_remove_album_songs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albumTrack', models.CharField(max_length=250)),
                ('trackDuration', models.CharField(max_length=10)),
                ('songs', models.FileField(null=b'I00\n', upload_to='')),
            ],
        ),
    ]