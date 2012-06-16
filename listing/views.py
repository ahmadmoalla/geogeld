from django.shortcuts import render_to_response
from django.template import RequestContext
from listing.forms import PostListingForm
from django.http import HttpResponseRedirect
from accounts.models import UserProfile
from listing.models import Listing
from django.contrib.auth.decorators import login_required

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
        post_listing_form = PostListingForm(request.POST)
        if post_listing_form.is_valid():
            # post the listing
            pass

    else:
        user_profile = UserProfile.objects.get(user_ptr_id=request.user.id)
        data = {
                'user': user_profile.user_ptr_id,
                'country': user_profile.country,
                'city': user_profile.city,
                'address': user_profile.address,
                'zipcode': user_profile.zipcode,
                'mobile_number': user_profile.mobile_number,
                }
        post_listing_form = PostListingForm(initial=data)

    context = {
               'post_listing_form': post_listing_form,
               }
    
    return render_to_response(template_name, context, RequestContext(request))