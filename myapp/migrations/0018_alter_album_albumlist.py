# Generated by Django 4.0 on 2022-08-03 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_album_albumlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumlist',
            field=models.ForeignKey(null=b'I00\n', on_delete=django.db.models.deletion.CASCADE, to='myapp.albumlist'),
        ),
    ]