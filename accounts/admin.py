from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from django.conf.__init__ import settings

from accounts.models import UserProfile
 
 
class UserProfileAdmin(geoadmin.OSMGeoAdmin):
    default_lon = settings.BERLIN_CENTER_LONGTITUDE
    default_lat = settings.BERLIN_CENTER_LATITUDE
    default_zoom = 11
 
admin.site.register(UserProfile, UserProfileAdmin)