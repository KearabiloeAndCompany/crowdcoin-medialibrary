# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-16 10:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('file', models.FileField(upload_to=b'')),
            ],
            options={
                'permissions': (('view_media', 'Can view media'),),
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('media', models.ManyToManyField(to='cms.Media')),
            ],
            options={
                'permissions': (('view_playlist', 'Can view playlist'),),
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
                ('stamp', models.DateTimeField(auto_now_add=True)),
                ('media', models.ManyToManyField(to='cms.Media')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Playlist')),
            ],
            options={
                'permissions': (('view_purchase', 'Can view purchase'),),
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('view_user', 'Can view user'),)},
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='media',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
