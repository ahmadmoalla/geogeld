from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from django.conf.__init__ import settings

from listing.models import Listing, Category

class CategoryAdmin(admin.ModelAdmin):
    pass


class ListingAdmin(geoadmin.OSMGeoAdmin):
    default_lon = settings.BERLIN_CENTER_LONGTITUDE
    default_lat = settings.BERLIN_CENTER_LATITUDE
    default_zoom = 11

admin.site.register(Listing, ListingAdmin)
admin.site.register(Category, CategoryAdmin)