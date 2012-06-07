# -*- coding: utf-8 -*-
from django import forms
from listing.models import Listing

class PostListingForm(forms.ModelForm):
    class Meta:
        model = Listing