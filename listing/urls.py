from django.conf.urls import patterns, url

urlpatterns = patterns('listing.views',
    url(r'^search/$', 'search'),
    url(r'^post/$', 'post_listing'),
)