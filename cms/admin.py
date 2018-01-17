from django.contrib import admin
from cms.models import *
from django.contrib.auth.admin import UserAdmin
from tastypie.admin import ApiKeyInline

class UserModelAdmin(UserAdmin):
	inlines = UserAdmin.inlines + [ApiKeyInline]

class PlaylistAdmin(admin.ModelAdmin):
	list_filter = (('media', admin.RelatedOnlyFieldListFilter),)

	def get_queryset(self, request):
		qs = Playlist.objects.all()
		if request.user.is_superuser:
			return qs
		return qs.filter(user=request.user)

class MediaAdmin(admin.ModelAdmin):

	def get_queryset(self, request):
		qs = Media.objects.all()
		if request.user.is_superuser:
			return qs
		return qs.filter(user=request.user)

# Register your models here.
admin.site.register(User,UserModelAdmin)
admin.site.register(Playlist,PlaylistAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Purchase)