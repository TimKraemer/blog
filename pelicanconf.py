#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pilkit.processors import *

AUTHOR = u'Tim Krämer'
SITENAME = u'Tim in Boston'
SITEURL = ''
RELATIVE_URLS = False
TYPOGRIFY = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'de'

THEME = 'themes/SoMA'
PATH = 'content'
PLUGINS=['plugins.share_post', 'plugins.gallery', 'plugins.thumbnailer']

RESIZE = [
    ('gallery', '_thumbs', [SmartResize(180, 180)]), # Path within images to resize, Thumbnail folder suffix (Empty to overwrite), pilkit settings
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

AUTHORS_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
