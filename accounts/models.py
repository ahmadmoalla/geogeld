from django.db import models
from django.contrib.gis.db import models  as geomodels
from django.contrib.auth.models import User
from django.conf.__init__ import settings


class UserProfile(User):
    ''' User profile 
        Represents a user that has account in the system
    '''
    
    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'

    country = models.CharField(max_length=255, null=False, blank=False, help_text="Country")
    city = models.CharField(max_length=255, null=False, blank=False, default='Berlin', help_text="City")
    zipcode = models.CharField(max_length=20, null=False, blank=False, default=12167, verbose_name="Zip code", help_text="Zip code")
    address = models.CharField(max_length=1024, null=False, blank=False, help_text="Address")
    birth_date = models.DateField(help_text="Birth date")
    mobile_number = models.CharField(max_length=30, help_text="Mobile number")
    location = geomodels.PointField(srid=settings.SPHERICAL_MERCATOR, help_text="Location")
    
    objects = geomodels.GeoManager()
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __repr__(self):
        return "<UserProfile: %s %s>" % (self.first_name, self.last_name)