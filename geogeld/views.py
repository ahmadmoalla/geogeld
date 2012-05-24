from django.shortcuts import render_to_response
from django.template import RequestContext

from listing.models import Listing

def home(request, template_name='geogeld/index.html'):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render_to_response(template_name, context, RequestContext(request))