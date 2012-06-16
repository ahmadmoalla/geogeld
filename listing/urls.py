from django.conf.urls import patterns, url

urlpatterns = patterns('listing.views',
    url(r'^search/$', 'search'),
    url(r'^post/$', 'listing_post'),
    url(r'^(\d+)/reply/$', 'listing_reply'),
    url(r'^(\d+)/details/$', 'listing_details'),
)