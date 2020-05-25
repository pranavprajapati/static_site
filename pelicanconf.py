#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pranav Prajapati'
SITENAME = 'Data Learnings'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ["uploads", "admin", "images"]
# Optional - if you want Netlify CMS
TEMPLATE_PAGES = {"admin/index.html": "admin/index.html"}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

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

DEFAULT_PAGINATION = False

# Overwrites the output directory (/output) when generating new files
DELETE_OUTPUT_DIRECTORY = True

# path/to/theme/folder or name or installed via pelican-themes
THEME = "theme/pelican-bootstrap3"

PLUGIN_PATHS = ['plugins/' ,]
PLUGINS = ['i18n_subsites' ,]

JINJA_ENVIRONMENT = { 'extensions': ['jinja2.ext.i18n'], }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Change to True if you want RSS
FEED_ALL_ATOM = False
FEED_ALL_RSS = False