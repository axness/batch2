'''
Created on Jun 1, 2018

@author: nexii
'''
from django.conf.urls import url
from book.views import index, first, first_h2, get_name, publishers, pub_detail, add_pub
app_name = 'book'
urlpatterns = [
    url(r'^$', index),
    url(r'^first/$', first),
    url(r'^first/h2/', first_h2),
    url(r'^name/$', get_name),
    url(r'^addpub/$', add_pub),
    url(r'^publishers/$', publishers, name='publisher'),
    url(r'^publishers/(?P<id>[0-9]+)$', pub_detail),
]
