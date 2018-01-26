#!/usr/bin/env python
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from firststep.models import Category, Page

def populate():

    python_pages =[
        {"title":"Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/",
         "views":7},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/",
         "views":3},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/",
         "views":1} ]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views":21},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/",
         "views":13},
        {"title":"How to Tango with Django",
         "url":"http://www.tangowithdjango.com/",
         "views":79} ]

    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/",
         "views":59},
        {"title":"Flask",
         "url":"http://flask.pocoo.org",
         "views":11} ]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages} }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"],p["views"])
             
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    if c.name=='Python':
        c.view=128
        c.likes=64
    elif c.name=='Django':
        c.view=64
        c.likes=32
    elif c.name=='Other Frameworks':
        c.view=32
        c.likes=16
    c.save()   
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
