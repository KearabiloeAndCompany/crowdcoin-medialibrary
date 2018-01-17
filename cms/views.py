# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from cms.models import *

# Create your views here.
class HomeView(View):
    template_name = "home.html"
    
    def get(self, request, *args, **kwargs):
        context ={}
        playlist = Playlist.objects.filter()
        context['playlists'] = playlist
        request.session['active_side_pane'] = 'Home'
        return render(request, self.template_name, context)

class PurchasesView(LoginRequiredMixin,View):
    template_name = "purchases.html"
    
    def get(self, request, *args, **kwargs):
        context ={}
        context['purchases'] = Purchase.objects.filter(user=request.user)
        request.session['active_side_pane'] = 'Purchases'
        return render(request, self.template_name, context)

class PlaylistView(View):
    template_name = "playlist.html"
    
    def get(self, request, *args, **kwargs):
        context ={}
        slug = kwargs.get('slug')
        playlist = get_object_or_404(Playlist,id=slug)
        context['playlist'] = playlist
        request.session['active_side_pane'] = 'Playlist'
        return render(request, self.template_name, context)

class MediaView(LoginRequiredMixin,View):
    template_name = "media.html"
    
    def get(self, request, *args, **kwargs):
        context ={}
        slug = kwargs.get('slug')
        media = get_object_or_404(Media,id=slug)
        context['active_media'] = media
        request.session['active_side_pane'] = media.name
        return render(request, self.template_name, context)
