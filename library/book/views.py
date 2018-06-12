# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from book.models import Publisher
from django.template import loader
from book.forms import PulisherForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def get_name(request):
    return render(request, "name.html", {'name':'Nageswararao'})

def first(request):
    pb_obj = Publisher.objects.all()
    msg = "<table border=2>"
    for obj in pb_obj:
        msg = msg+"<tr><td>"+obj.name+"</td><td>"+obj.url+"</td></tr>"
    msg = msg+"</table>"
    return HttpResponse(msg)

def first_h2(request):
    template = loader.get_template('first.html')

    return HttpResponse(template.render())

def publishers(request):
    pub_list = Publisher.objects.all()
    return render(request, 'pub.html', {'pub_list':pub_list}) 
def pub_detail(request, *args, **kwargs):
    pub = Publisher.objects.get(id=kwargs['id'])
    return render(request, 'pub_detail.html', {'pub123': pub})

def add_pub(request):
    form_obj = PulisherForm(request.GET)
    if form_obj.is_valid():
        form_obj.save()
        """
        data = form_obj.clean_data
        db_obj = Publisher()
        db_obj.name = data['publisher_name']
        db_obj.url = data['url']
        db_obj.email = data['email']
        db_obj.save()
        
        """
        return render(request, 'success.html', {'name': 'Publisher'})
    form_obj = PulisherForm()
    return render(request, 'addpub.html', {'form123': form_obj})
    
