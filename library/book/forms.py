'''
Created on Jun 8, 2018

@author: nexii
'''
from django import forms
from book.models import Publisher
"""
class PulisherForm(forms.Form):
    publisher_name = forms.CharField(max_length=50)
    url = forms.URLField()
    email = forms.EmailField()
    
"""
class PulisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        #exclude = ['email']#fields = '__all__' or fields = ['name', 'email']
        fields = '__all__'