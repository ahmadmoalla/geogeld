from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile


class HouseKeeping(models.Model):
    '''
    DELETE THIS COMMENT WHEN YOU START
    House keeping listing will have:
    User
    description
    required skills
    location
    country
    city
    zipcode
    address
    mobile number (must match user mobile)
    payment: fixed price or per hour
    number of working hours required (if payment is per hour)
    payment per hour or fixed depend on the payment option
    
    '''
    class Meta:
        verbose_name = 'house_keeping'
        verbose_name_plural = 'house_keepings'

    def __unicode__(self):
        return self.title