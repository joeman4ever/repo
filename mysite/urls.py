from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# Examples:
    	# url(r'^$', 'mysite.views.home', name='home'),
    	# url(r'^blog/', include('blog.urls')),
   
    # Enable URL patterns for installed applications
    url(r'^picsite/', include('picsite.urls', namespace="picsite")),
	# url(r'^polls/', include('polls.urls', namespace="polls")),
	
	# Enable URL patterns for the admin portal
	url(r'^admin/', include(admin.site.urls)),

	# User auth URLS
	#url(r'^accounts/login/$', 'picsite.views.login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
