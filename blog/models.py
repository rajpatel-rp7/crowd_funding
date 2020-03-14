# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Entry(models.Model):
    DRAFT = 'D'
    HIDDEN = 'H'
    PUBLISHED = 'P'
    ENTRY_STATUS = (
        (DRAFT, 'Draft'),
        (HIDDEN, 'Hidden'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    quotes = models.CharField(max_length=255, null=True, blank=True)
    summary = models.TextField(max_length=1500, null=True, blank=True)
    status = models.CharField(max_length=10, choices=ENTRY_STATUS)
    start_publication = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(User, null=True, blank=True, related_name="+")
    blog_cover_image = models.ImageField(upload_to='blog/%Y/%m/%d', default=True)
    middle_image1 = models.ImageField(upload_to='blog/middle_image1/%Y/%m/%d', default=True)
    middle_image2 = models.ImageField(upload_to='blog/middle_image2/%Y/%m/%d', default=True)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title
