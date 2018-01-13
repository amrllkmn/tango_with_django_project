# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! <br/> <a href='/firststep/about/'>About</a>")

def about(request):
    return HttpResponse("This quaint application is part of the individual assessment for the Web App Development 2 Course. <br/> <a href='/firststep/'>Index</a>")
