from django.shortcuts import render_to_response
from django.template import RequestContext
from listing.forms import PostListingForm
from django.http import HttpResponseRedirect

def search(request, template_name='listing/index.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))

def post_listing(request, template_name='listing/post_listing.html'):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/registration/')
    
    post_listing_form = PostListingForm()
    context = {
               'post_listing_form': post_listing_form,
               }
    return render_to_response(template_name, context, RequestContext(request))