#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Renata'
SITENAME = "Renata's blog"
SITEURL = 'https://rsip22.github.io/blog/'
HTML_LANG = 'en'

THEME = './themes/pelican-simplegrey'
# BOOTSTRAP_THEME = 'simplegrey'

HIDE_CATEGORIES_FROM_MENU = True
DISPLAY_PAGES_ON_MENU = False

PATH = 'content'
WITH_FUTURE_DATES = False

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

PELICAN_SIMPLEGREY_TWITTER_CARD_ACCOUNT = 'rsip22'
TWITTER_USERNAME = 'rsip22'

OPEN_GRAPH_IMAGE = 'opengraph_600.jpg'
STYLES_CSS_FILE = 'styles.css'

# Blogroll
LINKS = (('My portfolio', 'https://rsip22.github.io/portfolio'),
         ('Outreachy', 'http://outreachy.org/'),
         ('PyLadies Porto Alegre', 'https://pyladiespoa.pythonanywhere.com'))

# Social widget
SOCIAL = (('Twitter', 'https://www.twitter.com/rsip22'),
          ('Github', 'https://www.github.com/rsip22'),
          ('Linkedin', 'https://linkedin.com/in/rsip22'))

DEFAULT_PAGINATION = 5

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
TAGS_SAVE_AS = 'tags.html'

STATIC_PATHS = ['img']

PLUGIN_PATHS = ['./.plugins/pelican-plugins']

PLUGINS = [
        'gzip_cache',
        'post_stats',
        'related_posts',
        'sitemap',
    ]

RESPONSIVE_IMAGES = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 1
    },
    'changefreqs': {
        'articles': 'hourly',
        'indexes': 'daily',
        'pages': 'weekly'
    }
}

# READ_MORE_LINK = 'Keep reading -->'

RELATED_POSTS_MAX = 2

"""
FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
)
"""
RELATIVE_URLS = False
