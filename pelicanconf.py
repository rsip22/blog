#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Renata'
SITENAME = "Renata's blog"
SITEURL = ''

THEME = 'themes/pelican-simplegrey'
# BOOTSTRAP_THEME = 'simplegrey'

HIDE_CATEGORIES_FROM_MENU = True
DISPLAY_PAGES_ON_MENU = False

PATH = 'content'
WITH_FUTURE_DATES = False

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'

PELICAN_SIMPLEGREY_TWITTER_CARD_ACCOUNT = 'rsip22'
TWITTER_USERNAME = 'rsip22'
OPEN_GRAPH_IMAGE = 'opengraph.png'

# Blogroll
LINKS = (('Outreachy', 'http://outreachy.org/'),
         ('PyLadies Porto Alegre', 'https://pyladiespoa.pythonanywhere.com'))

# Social widget
SOCIAL = (('Quitter', 'https://www.quitter.se/rsip22'),
          ('Twitter', 'https://www.twitter.com/rsip22'),
          ('Github', 'https://www.github.com/rsip22'),)

DEFAULT_PAGINATION = 5

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
TAGS_SAVE_AS = 'tags.html'

STATIC_PATHS = ['img']

"""
FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
)
"""
RELATIVE_URLS = False
