import re
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from accounts.forms import RegistrationForm

@login_required(login_url='accounts/login_or_registration/')
def profile(request, template_name='accounts/profile.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))

def login_or_registration(request, template_name='accounts/login_or_registration.html'):
    registration_form = RegistrationForm()
    login_form = AuthenticationForm()
    
    if request.method == 'POST':
        # clean the location field from the SRID=...; part which olwidget.js(?) inserts
        post_data = dict(request.POST) # we need this because QueryDict is immutable
        title = request.POST.get('title')
        category = request.POST.get('category')
        
        location_string = ''.join(post_data.get('location'))  # use ''.join() to stringify the list
        if location_string:
            # Extract the SRID=...; part of the location value
            post_data['location'] = location_string.replace(''.join(re.findall('(SRID=.*;)POINT', location_string)), '') 

        registration_form = RegistrationForm(request.POST)
        # authenticate and log the user in after the account in created
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            username = registration_form.cleaned_data['username']
            password = registration_form.cleaned_data['password']
            new_user.set_password(password)
            new_user.save()
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            return HttpResponseRedirect('/listings/post/?title=%s&category=%s' % (title, category))
        
    title = request.GET.get('title')
    category = request.GET.get('category')
    
    context = {
               "registration_form": registration_form,
               "login_form": login_form,
               "title": title,
               "category": category,
               }
    
    return render_to_response(template_name, context, RequestContext(request))