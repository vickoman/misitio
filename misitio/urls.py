from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',    	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('misitio.apps.main.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}), 
)
