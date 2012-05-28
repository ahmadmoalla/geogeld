from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from django.conf.__init__ import settings
from django.contrib.auth.models import User, Group
#from django.contrib.sites.models import Site

from accounts.models import UserProfile


class UserProfileAdmin(geoadmin.OSMGeoAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'country', 'city', 'zipcode', 
                    'address', 'location')
    list_display_links = list_display
    
    default_lon = settings.BERLIN_CENTER_LONGTITUDE
    default_lat = settings.BERLIN_CENTER_LATITUDE
    default_zoom = 11


admin.site.unregister(User)
admin.site.unregister(Group)
#admin.site.unregister(Site)

admin.site.register(UserProfile, UserProfileAdmin)
