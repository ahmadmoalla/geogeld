from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^login/?next=(?P<redirect_field_name>.*)/', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),

    
    url(r'^profile/', include('accounts.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^listings/', include('listing.urls')),

    url(r'^$', 'geogeld.views.home', name='home'),
)