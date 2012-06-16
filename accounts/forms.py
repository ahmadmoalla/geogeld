# -*- coding: utf-8 -*-
from django import forms
from olwidget.forms import MapModelForm

from accounts.models import UserProfile
from geogeld.settings import BERLIN_CENTER_LATITUDE, BERLIN_CENTER_LONGTITUDE,\
    SPHERICAL_MERCATOR

class RegistrationForm(MapModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['first_name', 'last_name', 'email', 'username', 
                                'password', 'country', 'city', 'address', 'zipcode',
                                'birth_date', 'mobile_number', 'location']
        
    class Meta:
        model = UserProfile
        exclude = ('user_permissions', 'groups', 'is_active', 'is_staff', 'is_superuser', 
                    'date_joined', 'last_login',)
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
    
        
#    first_name = forms.CharField(max_length=255, help_text="")
#    last_name = forms.CharField(max_length=255, help_text="")
#    mobile_number = forms.CharField(max_length=30, help_text="")
#    country = forms.CharField(max_length=255, help_text="")
#    email = forms.CharField(max_length=255, help_text="")
#    city = forms.CharField(max_length=255, help_text="")
#    zipcode = forms.CharField(max_length=20, help_text="")
#    address = forms.CharField(max_length=1024, help_text="")
#    nickname = forms.CharField(max_length=255, help_text="")
#    birth_date = forms.DateField(widget=AdminDateWidget(), help_text="")
