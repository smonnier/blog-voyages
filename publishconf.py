#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

STATIC_PATHS.append("wp-content")
IGNORE_FILES = []

DELETE_OUTPUT_DIRECTORY = False # Because we don't want to erase the wp-images

DISQUS_SITENAME = SITEDOMAIN
DISQUS_SHORTNAME = "vivianevoyages"

GTM = "GTM-T5BGFK2"

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
