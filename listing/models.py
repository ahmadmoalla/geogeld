from django.db import models
from django.contrib.gis.db import models as geomodels

from django.conf.__init__ import settings
from accounts.models import UserProfile


PAYMENT_TYPE = {
        'HOURLY': 1,
        'FIXED_PRICE': 2,
}

PAYMENT_TYPE_CHOICES = (
        (1, 'HOURLY'),
        (2, 'FIXED PRICE'),
)

class Category(models.Model):
    '''
    Category
    Represents a category into which a job offer may fall
    '''
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=255, help_text="")
    
    def __unicode__(self):
        return self.name
    
    def listing_count(self):
        listing_count = Listing.objects.filter(category=self.id).count()
        return "(%d)" % (listing_count,)

class Listing(models.Model):
    '''
    Listing
    Represents a job offer
    '''
    class Meta:
        verbose_name = 'listing'
        verbose_name_plural = 'listings'

    user = models.ForeignKey(UserProfile, help_text="User")
    category = models.ForeignKey(Category, default=1, help_text="")
    title = models.CharField(max_length=1024, null=False, blank=False, help_text="")
    description = models.TextField(null=True, blank=True, help_text="")
    required_skills = models.TextField(null=True, blank=True, verbose_name="Required skills", help_text="")
    location = geomodels.PointField(srid=settings.SPHERICAL_MERCATOR, help_text="Location of the job")
    country = models.CharField(max_length=255, null=False, blank=False, default="Germany", help_text="")
    city = models.CharField(max_length=255, null=False, blank=False, default="Berlin", help_text="")
    zipcode = models.CharField(max_length=20, null=False, blank=False, default=12167, verbose_name="Zip code", help_text="")
    address = models.CharField(max_length=1024, null=False, blank=False, help_text="")
    mobile_number = models.CharField(max_length=30, verbose_name="Mobile number", help_text="")
    payment_type = models.IntegerField(null=False, blank=False, 
                                    choices=PAYMENT_TYPE_CHOICES, default=PAYMENT_TYPE['HOURLY'],
                                    verbose_name="Payment type",  
                                    help_text="Payment type (Fixed or hourly)")
    working_hours = models.IntegerField(verbose_name="Working hours", help_text="Approximate number of hours required")
    payment_rate = models.IntegerField(verbose_name="Payment rate", help_text="Payment per hour or fixed price")

    objects = geomodels.GeoManager()
    
    def __unicode__(self):
        return self.title