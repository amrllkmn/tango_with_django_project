# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def about(request):
    return HttpResponse("This quaint application is part of the individual assessment for the Web App Development 2 Course <a href='/firststep/'>Index</a>")
