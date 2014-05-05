#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://tim-kraemer.de/blog'

PLUGINS += ['plugins.optimize_images', 'plugins.gzip_cache', 'plugins.sitemap']
#PLUGINS += ['plugins.wc3_validate'] #if there is a CRITICAL: HTTP Error 500: Internal Server Error, comment this line out

FEED_ALL_RSS = 'feeds/all.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
