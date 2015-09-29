""" Controller for Picsite app using functional views; class-based views saved
for reusable views. Each view maps to a url pattern defined in urls.py. Only
vars in 'context' of a view can be accessed by corresponding html template. """

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from picsite.models import Photo, Album
from picsite.forms import PhotoForm, AlbumForm, AlbumForm2

from django import forms
from django.contrib.auth.forms import UserCreationForm

# Controller for index.html page that declares one var as context to be
# render(ed) at picsite/index.html page

# View for landing/index page. It displays login page & redirects to home once authenticated
@login_required() #requires login before seeing this section
def index(request):
	title = "Login page"
	context = {
		'title': title
	}
	return HttpResponseRedirect(reverse('picsite:home'))
	# return render(request, 'picsite/photolist.html', context)


# View for landing page once logged in -- this is the photo gallery page
@login_required() #requires login before seeing this section
def home(request):
	title = "Welcome to the home page!"
	# current_user = request.user.id

	#process the form and grab uploaded file and then set owner to request.user
	if request.method=="POST":
		photo = Photo(owner=request.user)
		form = PhotoForm(request.POST, request.FILES, instance=photo)
		# form.owner = request.user.id
		if form.is_valid():
			form.save()

			# Defining page to return to after successful photo upload
			return HttpResponseRedirect(reverse('picsite:home'))
	
	# if nothing was submitted, return to the photo upload form
	else:
		form = PhotoForm()
	# retrieve all photos and store them in a list called images
	images = Photo.objects.filter(owner=request.user.id)
	context = {
		'title': title,
		'form': form,
		'images': images
	}
	return render(request, 'picsite/home.html', context)


# Retrieve 5 most recently uploaded photos and link to each - order by upload date
@login_required() #requires login before seeing this section
def photolist(request):
	images = Photo.objects.filter(owner=request.user.id)
	latest_photos = images.order_by('-uploadDate')[:5]
	title = "Here are the 5 most recently uploaded photos:"
	context = {
		'latest_photos': latest_photos,
		'title': title
	}
	return render(request, 'picsite/photolist.html', context)


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST) # fills in registration form with submitted info
		if form.is_valid(): # if form was submitted with legitimate data
			new_user = form.save() # save form info as 'new_user'
			# where to go after user successfully registers
			return HttpResponseRedirect(reverse('picsite:registered')) #'reverse' bit is important!
		# if form fails validation, display error next to fields
		else:
			print form.errors
			# return HttpResponse('form submission is NOT valid')
	# if nothing was posted, re-display the blank registration form
	else:
		form = UserCreationForm()

	context = {
		'form': form
	}
	return render(request, 'registration/register.html', context)

# simply displays a registration success page
def registered(request):
	title = "Registration success page"
	context = {
		'title': title
	}
	return render(request, 'registration/registered.html', context)

# Creating albums
# @markmhx -- here's the "controller" for the album page. It's essentially same 
# as the home controller above.
def albums(request):
	title = "Create an album"
	#process the form and grab uploaded file and then set owner to request.user
	if request.method=="POST":
		albumInstance = Album(owner=request.user)
		form = AlbumForm(request.POST, request.FILES, instance=albumInstance)
		# form.owner = request.user.id
		if form.is_valid():
			# album = Album.objects.create(owner=request.user)
			# for photo in request.POST.getlist('photos'):
			# 	Album.photos.add(photo)
			# 	p1.save()

			form.save()

			# Defining page to return to after successful album creation
			return HttpResponseRedirect(reverse('picsite:albums'))
	
	# if nothing was submitted, return to the album creation form
	else:
		form = AlbumForm()
	# retrieve all albums and store them in a list called albums
	albums = Album.objects.filter(owner=request.user.id)
	# pics = request.POST.getlist('photos')
	photos = Photo.objects.filter(owner=request.user.id)
	context = {
		'title': title,
		'form': form,
		'albums': albums,
		'photos': photos
	}
	return render(request, 'picsite/albums.html', context)

# page for uploading photos into an album
def upload(request):
	title = "Add photos to your album"
	
	#process the form and grab uploaded file and then set owner to request.user
	if request.method=="POST":
		album = Album(owner=request.user)
		form = AlbumForm2(request.POST, request.FILES, instance=album)
		# form.owner = request.user.id
		if form.is_valid():
			for photo in request.POST.getlist('photos'):
				p1 = Album(owner=request.user)
				p1.save()

			form.save()

			# Defining page to return to after successful photo upload
			return HttpResponseRedirect(reverse('picsite:upload'))
	
	# if nothing was submitted, return to the photo upload form
	else:
		form = AlbumForm2()
	# retrieve all photos and store them in a list called images
	albums = Album.objects.filter(owner=request.user.id)
	context = {
		'title': title,
		'form': form,
		'albums': albums
	}
	return render(request, 'picsite/photo_upload.html', context)


# Old views not currently in use

# View for logging in a user
# def login_view(request):
# 	title = "Log in page"
# 	context = {
# 		'title': title
# 	}
# 	context.update(csrf(request))
# 	return render(request, 'picsite/login.html', context)

# Authenticate the user, make sure user exists - step 1
# def auth_view(request):
# 	# username = request.POST.get('username', '')
# 	# password = request.POST.get('password', '')
# 	username = request.POST['username']
# 	password = request.POST['password']
# 	user = authenticate(username=username, password=password)
# 	context = {
# 		'username': username,
# 		'password': password,
# 		'user': user
# 	}
# 	# Actually log in the user, if s/he exists - step 2
# 	if user is not None:
# 		if user.is_active:
# 			login(request, user)
# 			return HttpResponseRedirect(reverse('picsite:home'))
# 		else:
# 			return HttpResponse('Hmm, looks like your account is disabled.')
# 	else:
# 		return render(request, 'picsite/accounts/invalid_login.html', context)

# What to do once user is logged in
# @login_required() #requires login before seeing this section
# def loggedin(request):
# 	full_name = request.user.username
# 	context = {
# 		'full_name': full_name
# 	}
# 	return render(request, 'picsite/accounts/loggedin.html', context)

# def invalid_login(request):
# 	return render(request, 'picsite/accounts/invalid_login.html', context)

# What to do when user logs out
# def logout_view(request):
# 	context = {}
# 	logout(request)
# 	return render(request, 'picsite/accounts/logout.html', context)



# captures photo_id attribute of photo and uses that in URL and as pk
# @login_required()
# def detail(request, id):
# 	# photo var represents a photo with all its attributes allowing for dot-
# 	# notation like in photo.photo_name or photo.photo_id
# 	photo = get_object_or_404(Photo, pk=id)
# 	title = "This is the detail page for %s." % photo.name
# 	context = {
# 		'photo': photo,
# 		'title': title
# 	}
# 	return render(request, 'picsite/detail.html', context)

# @login_required()
# def more(request, id):
# 	photo = get_object_or_404(Photo, pk=photo.id)
# 	title = "You're looking at the more details page for %s." % photo.name
# 	context = {
# 		'photo': photo,
# 		'title': title
# 	}
# 	return render(request, 'picsite/more.html', context)