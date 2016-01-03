# URLconf for Picsite app. The URL patterns map to corresponding views in view.py

# from django.conf import settings
# from django.conf.urls.static import static

from django.conf.urls import patterns, url, include
from django.contrib.auth.views import logout, password_change, password_change_done

from picsite import views

# defining a list of url regex patterns to be used in processing requests
urlpatterns = [
	# ex: /picsite/ ; only requires http request as variable in url
	# format: url(regex pattern, function in views.py to handle the request, friendly name)
	url(r'^$', views.index, name='index'),

	# ex: /picsite/photolist/ or /picsite/home ; only requires http request
	url(r'^photolist/$', views.photolist, name='photolist'),
	url(r'^home/$', views.home, name='home'),
	url(r'^albums/$', views.albums, name='albums'),
	url(r'^photo_upload/$', views.upload, name='upload'),
	url(r'^registration/register/$', views.register, name='register'),
	url(r'^registration/registered/$', views.registered, name='registered'),

	# ex: /picsite/10/ ; dw+ is regex requiring an integer in url pattern in
	# addition to http request as variables
	# photo_name is charField, an attribute of an uploaded photo per Photo model
	#?P = required syntax for named views
	# url(r'^(?P<photo_id>\d+)/$', views.detail, name='detail'), #no longer needed

	#ex: /picsite/john/more/
	# url(r'^(?P<photo_id>\d+)/more/$', views.more, name='more'), #no longer needed

	# Using Django's built-in views. The pattern below includes the ff URL patterns:
	# ^login/$ [name='login']
	url(r'^logout/$', logout, {'template_name': 'picsite/accounts/logged_out.html'}),
	url(r'^password_change/$', password_change, {'template_name': 'picsite/accounts/password_change_form.html', 'post_change_redirect': 'picsite:password_change_done'}),
	url(r'^password_change/done/$', password_change_done, {'template_name': 'picsite/accounts/password_change_done.html'}),
	# ^password_reset/$ [name='password_reset']
	# ^password_reset/done/$ [name='password_reset_done']
	# ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
	# ^reset/done/$ [name='password_reset_complete']
	url(r'^', include('django.contrib.auth.urls'))

	# User auth URLS
	# url(r'^accounts/login_view/$', views.login_view, name='login_view'),
	# url(r'^accounts/auth/$', views.auth_view, name='auth_view'),
	# url(r'^accounts/logout_view/$', views.logout_view, name='logout_view'),
	# url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
	# url(r'^accounts/invalid_login/$', views.invalid_login, name='invalid_login')
]