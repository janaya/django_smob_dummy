from django.conf.urls.defaults import *
from django.contrib.auth.views import User
from django.views.generic.simple import redirect_to
from django.views.generic import DetailView, ListView
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


import logging

import os.path

urlpatterns = patterns('djsmobdummy.views',

    # turtle uris
#    url(r'^data/hub', 'triples_hub', name='triples_hub'),
    url(r'^data/person', 'triples_person', name='triples_person'),
#    url(r'^data/post', 'triples_posts', name='triples_posts'),
#    url(r'^data/post/(?P<slug>[-\w]+)/$', 'triples_post', name='triples_post'),
#    url(r'^data/followings', 'triples_followings', name='triples_followings'),
#    url(r'^data/followers', 'triples_followers', name='triples_followers'),
#    url(r'^data/preference', 'triples_preference', name='triples_preference'),
#    url(r'^data/preference/(?P<slug>[-\w]+)/$', 'triples_preferences', name='triples_preferences'),
#    url(r'^data/tagging', 'triples_taggings', name='triples_taggings'),
#    url(r'^data/tagging/(?P<slug>[-\w]+)/$', 'triples_tagging', name='triples_tagging'),

    # views
    url(r'^person/post/rssrdf', 'rssrdf_post', name='rssrdf_post'),
    
    # actions
    url(r'^callback', 'callback', name='callback'),
    
    # forms
    url(r'^post/add', 'add_post', name='add_post'),
    
)
