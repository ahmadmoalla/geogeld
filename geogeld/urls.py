from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^$', 'geogeld.views.home', name='home'),
    url(r'^accounts/', include('accounts.urls')),

)