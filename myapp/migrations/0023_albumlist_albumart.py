# Generated by Django 4.0 on 2022-08-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_rename_zipfile_albumlist_albumzip'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumlist',
            name='albumArt',
            field=models.FileField(null=b'I00\n', upload_to=''),
            preserve_default=b'I00\n',
        ),
    ]
