# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
	mobile = models.TextField(max_length=15, blank=True, null=True)
	birth_date = models.DateField(null=True, blank=True)

	class Meta:
		permissions = (("view_user", "Can view user"),)


class Media(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=250, null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	file = models.FileField()

	class Meta:
		permissions = (("view_media", "Can view media"),)

	def __str__(self):
		return self.name	


class Playlist(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=250)
	media = models.ManyToManyField(Media, blank=True)

	class Meta:
		permissions = (("view_playlist", "Can view playlist"),)

	def __str__(self):
		return self.name


class Purchase(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	reference = models.CharField(max_length=250)
	status = models.CharField(max_length=250)
	price = models.CharField(max_length=250)
	playlist = models.ForeignKey(Playlist, blank=True, null=True)
	media = models.ForeignKey(Media, blank=True, null=True)
	stamp = models.DateTimeField(auto_now_add=True, editable=True)

	class Meta:
		permissions = (("view_purchase", "Can view purchase"),)

	def __str__(self):
		return self.reference


def signals_import():
	""" A note on signals.
	The signals need to be imported early on so that they get registered
	by the application. Putting the signals here makes sure of this since
	the models package gets imported on the application startup.
	"""
	from tastypie.models import create_api_key

	models.signals.post_save.connect(create_api_key, sender=User)

signals_import()
