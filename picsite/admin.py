from django.contrib import admin
from picsite.models import Photo
from picsite.models import Album
# from picsite.models import Photo_Album


class PhotoAdmin(admin.ModelAdmin):
	fields = ['name', 'uploadDate', 'uploadPath']
	list_filter = ['name','id','uploadDate']
	search_fields = ['name','id','uploadDate']

class AlbumAdmin(admin.ModelAdmin):
	fields = ['name', 'dateCreated', 'description', 'category', 'owner']
	list_filter = ['name', 'id', 'dateCreated', 'category', 'owner']
	search_fields = ['name', 'id', 'dateCreated', 'category', 'owner']

# Register your models here.
admin.site.register(Photo, PhotoAdmin)

# Add more models individually, like so:
admin.site.register(Album, AlbumAdmin)