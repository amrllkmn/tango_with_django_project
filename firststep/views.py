# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Welcome to Rango! A web-app in progress.'}
    return render(request,'firststep/index.html',context=context_dict)

def about(request):
    context_dict = {'boldmessage' : 'This page is written by Amirul Lokman Jamaludin.'}
    return render(request, 'about/about.html',context=context_dict)
