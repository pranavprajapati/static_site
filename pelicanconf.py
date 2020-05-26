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
#LINKS = (('Pelican', 'http://getpelican.com/'),
 #        ('Python.org', 'http://python.org/'),
 #        ('Jinja2', 'http://jinja.pocoo.org/'),
 #        ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/pranavprajapati'),
          ('Twitter', 'https://twitter.com/Iam_pranav'),
          ('Linkedin', 'https://linkedin.com/in/prajapatipranav'),)

DEFAULT_PAGINATION = False

# Overwrites the output directory (/output) when generating new files
DELETE_OUTPUT_DIRECTORY = True

# path/to/theme/folder or name or installed via pelican-themes
THEME = "theme/pelican-bootstrap3"

PLUGIN_PATHS = ['plugins/' ,]
PLUGINS = ['i18n_subsites' ,'tag_cloud']

JINJA_ENVIRONMENT = { 'extensions': ['jinja2.ext.i18n'], }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

DISPLAY_TAGS_ON_SIDEBAR = False

TAG_CLOUD_STEPS=1 #number of different sizes of fonts in the tag cloud
TAG_CLOUD_MAX_ITEMS= 100 #number of different tags that can appear in tag cloud
TAG_CLOUD_SORTING= 'size' #how tags will be ordered in the tag cloud. Valid values: random, alphabetically, alphabetically-rev, size and size-rev
TAG_CLOUD_BADGE= True #If True, displays the number of articles in each tag

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = False

#DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

#DISPLAY_ARCHIVE_ON_SIDEBAR = True
RECENT_POST_COUNT = 2


# Change to True if you want RSS
FEED_ALL_ATOM = False
FEED_ALL_RSS = False