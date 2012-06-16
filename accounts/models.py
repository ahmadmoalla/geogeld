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

    country = models.CharField(max_length=255, null=False, blank=False, help_text="")
    city = models.CharField(max_length=255, null=False, blank=False, help_text="")
    zipcode = models.CharField(max_length=20, null=False, blank=False, verbose_name="Zip code", help_text="")
    address = models.CharField(max_length=1024, null=False, blank=False, help_text="")
    birth_date = models.DateField(help_text="format: dd/mm/yyyy")
    mobile_number = models.CharField(max_length=30, help_text="")
    location = geomodels.PointField(srid=settings.SPHERICAL_MERCATOR, help_text="")
    
    objects = geomodels.GeoManager()
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __repr__(self):
        return "<UserProfile: %s %s>" % (self.first_name, self.last_name)