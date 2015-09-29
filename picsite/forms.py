""" Import ModelForm subclass to leverage fields from Photo model in creating
form ojbect """

from django.forms import ModelForm, Textarea, ImageField, FileField
from picsite.models import Photo, Album
from django import forms
from django.utils.translation import ugettext_lazy as _


# Creating the form class by specifing model & field names for inheritance. 
# This is the form for uploading a photo
class PhotoForm(ModelForm):
	class Meta:
		model = Photo
		# These are fields from the Photo model. Can pick the ones needed for the form.
		# The labels displayed on page for each field come from the model tags
		fields = ['name', 'uploadDate', 'uploadPath', 'caption']

# This is the form for creating a photo album
class AlbumForm(ModelForm):
	photos = ImageField

	class Meta:
		model = Album
		# by not specifing fields = [], it'll include all fields from model
		# or you can specify below fields from model to include in the form
		fields = ['name', 'description', 'photos']
		widgets = {
			'description' : Textarea(attrs={'cols': 40, 'rows': 2}),
			# 'photos' : Textarea(attrs={'cols': 40, 'rows': 1})
		}
		labels = {
			'name': _('Album Name'),
			'description': _('Album Description'),
		}
		help_texts = {
			'name': _(' '),
		}
		error_messages = {
			'name': {
				'max_length': _('Your album name is wayyy too long!'),
			},
		}

# This is for the 2nd page of album creation
# AlbumForm2 is not currently being used.
class AlbumForm2(ModelForm):

	class Meta:
		model = Album
		# by not specifing fields = [], it'll include all fields from model
		# or you can specify below fields from model to include in the form
		fields = ['name', 'description', 'photos']
		widgets = {
			'description' : Textarea(attrs={'cols': 30, 'rows': 3}),
		}
		labels = {
			'name': _('Album Name'),
		}
		help_tets = {
			'name': _('Give your album a name.'),
		}
		error_messages = {
			'name': {
				'max_length': _('Your album name is wayyy too long!'),
			},
		}




# class UserForm(ModelForm):
# 	class Meta:
# 		model = User
# 		# # widgets is a forms feature that allows us to call out specific fields for 
# 		# special treatment
# 		fields = ['username', 'password']
# 		widgets = {
# 			'password': forms.PasswordInput(),
# 		}

