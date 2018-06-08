'''
Created on Jun 8, 2018

@author: nexii
'''
from django import forms

class PulisherForm(forms.Form):
    publisher_name = forms.CharField(max_length=50)
    url = forms.URLField()
    email = forms.EmailField()