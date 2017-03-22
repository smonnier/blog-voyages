#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Viviane'
SITENAME = u'Viviane Voyage...'
SITESUBTITLE = u'Écrire le monde'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

THEME = 'theme'
BOOTSTRAP = 'bootstrap-3.3.7-dist'
FONTAWESOME = 'font-awesome-4.6.3'

PLUGIN_PATHS = ['plugins/']
PLUGINS = [
        "neighbors",
        "random_article",
        "background",
        "voyages_tags"
    ]

RANDOM = "random.html"
STATIC_PATHS = ["images","fenetre.pdf"]
IGNORE_FILES = ['wp-content']

DEFAULT_LANG = u'fr'
USE_FOLDER_AS_CATEGORY = False
AUTHOR_SAVE_AS = False
DIRECT_TEMPLATES = ('index', 'archives','categories','tags')

BACKGROUND_PATH = "/content/images/backgrounds/"
BACKGROUND_URL = "images/backgrounds/"
BACKGROUND_DEFAULT = "images/home-bg.jpg"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

EXCLUDE_FROM_CATEGORY = {
    "voyages": {"peintures", "photo-du-mois", "photos"},
    "divers" : set(),
    "films": {"photos"},
    "livres" : {"un-an-en-irlande"}
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
