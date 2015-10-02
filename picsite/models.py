from django.db import models
import datetime

from django.contrib.auth.models import User #Using this built-in instead of creating my own


# Picsite models. A model is essentially a db table. Django auto-creates a 'joini table'
# to represent many-to-many relationships and names the table appName_fieldName_modelName
# No need to create a model for the join table, simply define relationships w/in the models
# Django autoo-creates an auto-incrementing primary key called id for each model (table)

# @markmhx - my initial photo upload form is based on this model below. The ImageField
# type is what presents end-user with option to upload a file.
class Photo(models.Model):
	# Creates picsite_photo db table with below fields as attributes for each photo
	# max_length is required for CharField; table name is picsite_photo
	name = models.CharField('name', max_length=50)
	uploadDate = models.DateTimeField('date', default=datetime.datetime.now, null=True)
	# upload_to is a sub-directory of MEDIA_ROOT defined in settings.py
	uploadPath = models.ImageField('path', upload_to= 'images/%Y/%m/%d/')
	caption = models.CharField(max_length=200, null=True)
	longitude = models.IntegerField(null=True)
	latitude = models.IntegerField(null=True)
	owner = models.ForeignKey(User)

	def __str__(self):
		return self.name


# Creating picsite_album db table that has ManyToMany relationship with picsite_photo
class Album(models.Model):
	name = models.CharField(max_length=50)
	dateCreated = models.DateTimeField('created', default=datetime.datetime.now, null=True)
	description = models.CharField(max_length=300, null=True)
	category = models.CharField(max_length=50, default="Test")
	photos = models.ManyToManyField(Photo, null=True)
	owner = models.ForeignKey(User)

	def __str__(self):
		return self.name

# Junction (aka "through") table for the photo-album ManyToMany relationship
# Django creates a table called: picsite_photo_album
# class Photo_Album(models.Model):
# 	album = models.ForeignKey(Album)
# 	photo = models.ForeignKey(Photo)
# 	owner = models.ForeignKey(User)

	# def __str__(self):
	# 	return self.album


# User_Photos is a junction table connecting a user to photos
# class User_Photos(models.Model):
# 	photoID = models.IntegerField('jpid', )
# 	userType = models.CharField(max_length=50, )
# 	userID = models.IntegerField('juid', )


# class User(models.Model):
# 	"""Defining user table"""
# 	username = models.CharField(max_length=200)
# 	password = models.CharField(max_length=50)

# 	def __str__(self):
# 		return self.name
