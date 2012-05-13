from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    '''
    DELETE THIS COMMENT WHEN YOU START
    a user profile will have:
    
    first name
    last name
    email
    city
    country
    zipcode
    address
    data of birth
    mobile number
    location (will be used later for google maps (what fields are necessary for that?)
    
    listings one to many relation
    
    '''
    class Meta:
        verbose_name = 'user_profile'
        verbose_name_plural = 'user_profiles'

    def __unicode__(self):
        return self.title