from django.shortcuts import render_to_response
from django.template import RequestContext

from listing.models import Listing
from accounts.models import UserProfile

NEIGHBOURHOOD_RADIUS = 3000 # 3 km

def home(request, template_name='geogeld/index.html'):
    listings = []
    if request.user.is_authenticated():
        userprofile = UserProfile.objects.get(id=request.user.id)
        loc = userprofile.location
        neighbourhood = loc.buffer(NEIGHBOURHOOD_RADIUS)
        listings = Listing.objects.filter(location__within=neighbourhood)
    else:
        listings = Listing.objects.all()

    context = {'listings': listings}
    return render_to_response(template_name, context, RequestContext(request))

def login(request, template_name='geogeld/login.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))