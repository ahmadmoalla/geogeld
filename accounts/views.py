from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import RegistrationForm

def profile(request, template_name='accounts/index.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))

def registration(request, template_name='accounts/registration.html'):
    registration_form = RegistrationForm()
    login_form = AuthenticationForm()
    
    context = {
               "registration_form": registration_form,
               "login_form": login_form,
               }
    return render_to_response(template_name, context, RequestContext(request))