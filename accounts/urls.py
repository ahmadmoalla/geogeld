from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    url(r'^profile/$', 'profile'),
    url(r'^login_or_registration/$', 'login_or_registration'),
)

