from django.shortcuts import render_to_response
from django.db.models import Q
from django.template import RequestContext

from listing.models import Listing
from accounts.models import UserProfile
from geogeld.settings import DISPLAY_LISTINGS_PER_PAGE
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

NEIGHBOURHOOD_RADIUS = 3000 # 3 km

def home(request, template_name='geogeld/index.html'):
    try:
        page = int(request.GET.get('page', 0))
    except ValueError:
        page = 0

#    start_listing = page*DISPLAY_LISTINGS_PER_PAGE
#    end_listing = start_listing + DISPLAY_LISTINGS_PER_PAGE
    
#    listings = Listing.objects.all()[start_listing:end_listing]
    listings = Listing.objects.all()
    
    if request.user.is_authenticated():
        userprofile = UserProfile.objects.get(id=request.user.id)
        loc = userprofile.location
        neighbourhood = loc.buffer(NEIGHBOURHOOD_RADIUS)
        listings = Listing.objects.filter(
                                        Q(location__within=neighbourhood) | 
                                        Q(location__disjoint=neighbourhood))\
                                  .distance(userprofile.location)\
                                  .order_by('location') # [start_listing:end_listing]
#        listings = Listing.objects.filter(Q(location__within=neighbourhood) | Q(location__disjoint=neighbourhood)).distance(userprofile.location).order_by('location')[start_listing:end_listing]

    paginator = Paginator(listings, DISPLAY_LISTINGS_PER_PAGE) # Show 25 contacts per page

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listings = paginator.page(paginator.num_pages)

    context = {
               'listings': listings,
               'paginator': paginator,
               'before_last_page': paginator.num_pages - 2,
               }
    return render_to_response(template_name, context, RequestContext(request))

def login(request, template_name='geogeld/login.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))