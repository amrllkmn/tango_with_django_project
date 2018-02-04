# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.defaultfilters import slugify

from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=128, unique=True)

    views= models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
    

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=200)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
