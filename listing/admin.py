from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from django.conf.__init__ import settings

from listing.models import Listing, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'listing_count',)
    list_display_links = list_display


class ListingAdmin(geoadmin.OSMGeoAdmin):
    default_lon = settings.BERLIN_CENTER_LONGTITUDE
    default_lat = settings.BERLIN_CENTER_LATITUDE
    default_zoom = 11
    
    list_display = ('title', 'user', 'zipcode', 'address', 'payment_type', 'working_hours', 
                    'payment_rate', 'location')
    list_display_links = list_display

admin.site.register(Listing, ListingAdmin)
admin.site.register(Category, CategoryAdmin)