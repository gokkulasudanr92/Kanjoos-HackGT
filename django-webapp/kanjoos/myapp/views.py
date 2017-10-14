from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

def home(req):
    return render(req, 'index.html', {'STATIC_URL': settings.STATIC_URL})
