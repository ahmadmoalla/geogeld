from django.conf.urls import patterns, url

urlpatterns = patterns('listing.views',
    url(r'^$', 'index_view', name='listing_index'),
)