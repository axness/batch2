# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length = 50)
    url = models.URLField(null = True, blank=True)
    email = models.EmailField()