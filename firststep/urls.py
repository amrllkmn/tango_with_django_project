# -*- coding: utf-8 -*-
from django.conf.urls import url
from firststep import views

urlpatterns = [
    url(r'^$',views.index, name ='index'),
    url(r'^about/',views.about, name = 'about')]
