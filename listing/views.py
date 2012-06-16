import re

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile
from listing.forms import PostListingForm
from listing.models import Listing

def search(request, template_name='listing/index.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))

def listing_details(request, listing_id, template_name='listing/listing_details.html'):
    listing = Listing.objects.get(id=listing_id)
    
    context = {"listing": listing}
    return render_to_response(template_name, context, RequestContext(request))

@login_required(login_url='/accounts/login_or_registration/')
def listing_reply(request, listing_id, template_name='listing/listing_reply.html'):

    listing = Listing.objects.get(id=listing_id)
    
    context = {"listing": listing}
    return render_to_response(template_name, context, RequestContext(request))

@login_required(login_url='/accounts/login_or_registration/')
def listing_post(request, template_name='listing/listing_post.html'):
    if request.method == 'POST':
        # clean the location field from the SRID=...; part which olwidget.js(?) inserts
        post_data = dict(request.POST) # we need this because QueryDict is immutable
        location_string = ''.join(post_data.get('location'))  # use ''.join() to stringify the list
        if location_string:
            post_data['location'] = location_string.replace(''.join(re.findall('(SRID=.*;)POINT', location_string)), '') # Extract the SRID=...; part of the location value

        post_listing_form = PostListingForm(request.POST)
        if post_listing_form.is_valid():
            new_listing = post_listing_form.save(commit=False)
            new_listing.user = request.user
            new_listing.save()
            # post the listing
            return HttpResponseRedirect('/')

    else:
        user_profile = UserProfile.objects.get(user_ptr_id=request.user.id)
        data = {
                'user': request.user.id,
                'title': request.GET.get('title'),
                'category': request.GET.get('category').lower(),
                'country': user_profile.country,
                'city': user_profile.city,
                'address': user_profile.address,
                'zipcode': user_profile.zipcode,
#                'mobile_number': user_profile.mobile_number,
                'mobile_number': 111111111111,
                }
        post_listing_form = PostListingForm(initial=data)

    context = {
               'post_listing_form': post_listing_form,
               }
    
    return render_to_response(template_name, context, RequestContext(request))