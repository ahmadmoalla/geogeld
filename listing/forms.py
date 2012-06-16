# -*- coding: utf-8 -*-
from django import forms
from olwidget.forms import MapModelForm
from olwidget.fields import EditableLayerField

from listing.models import Listing
from geogeld.settings import BERLIN_CENTER_LATITUDE, BERLIN_CENTER_LONGTITUDE,\
    SPHERICAL_MERCATOR


class PostListingForm(MapModelForm):

    def __init__(self, *args, **kwargs):
        super(PostListingForm, self).__init__(*args, **kwargs)
#        self.fields.keyOrder = ['first_name', 'last_name', 'email', 'username', 
#                                'password', 'country', 'city', 'address', 'zipcode',
#                                'birth_date', 'mobile_number', 'location']
        
    class Meta:
        model = Listing
        exclude = ('user', 'country', 'city', 'zipcode', 'address',)
#        exclude = ('user_permissions', 'groups', 'is_active', 'is_staff', 'is_superuser', 
#                    'date_joined', 'last_login',)
        options = {
                   'defaultZoom': 11,
                   'defaultLat': BERLIN_CENTER_LATITUDE,
                   'defaultLon': BERLIN_CENTER_LONGTITUDE,
                   'mapOptions': {
                                   'projection': 'EPSG:%d' % (SPHERICAL_MERCATOR,),
                                   'displayProjection': 'EPSG:%d' % (SPHERICAL_MERCATOR,),
                                   'controls': ['Navigation'],
                                }
                   }