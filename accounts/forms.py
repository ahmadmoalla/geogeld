# -*- coding: utf-8 -*-
from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=255, help_text="")
    last_name = forms.CharField(max_length=255, help_text="")
    mobile_number = forms.CharField(max_length=30, help_text="")
    country = forms.CharField(max_length=255, help_text="")
    email = forms.CharField(max_length=255, help_text="")
    city = forms.CharField(max_length=255, help_text="")
    zipcode = forms.CharField(max_length=20, help_text="")
    address = forms.CharField(max_length=1024, help_text="")
    nickname = forms.CharField(max_length=255, help_text="")
    birth_date = forms.DateField(help_text="")
